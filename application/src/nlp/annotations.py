'''
Created on Sep 2, 2014

@author: varun
'''
import cherrypy
from db.other.hgnc import Hgnc
from db.other.medic import Medic
from data.database import DBObject

class ManualAnnotations(DBObject):
    
    COLLECTION = "MANUAL_ANNOTATION"
    FK = ("PMID", "USERNAME")
    
    def __init__(self, pmid, username):
        DBObject.__init__(self, None)
        self._pmid = pmid
        self._username = username
        self._gene_annotations = []
        self._disease_annotations = []
        
    def set_gene_annotations(self, annotations):
        self._gene_annotations = annotations
        
    def get_gene_annotations(self):
        return self._gene_annotations
    
    def set_disease_annotations(self, annotations):
        self._disease_annotations = annotations
        
    def get_disease_annotations(self):
        return self._disease_annotations
    
    def create_or_update_gene_annotation(self, original_text, db_id, start_pos, end_pos):
        for annotation in self._gene_annotations:
            if annotation.db_id == db_id:
                existing_annotation = annotation
                break
            
        if existing_annotation:
            existing_annotation.add_mention(original_text, start_pos, end_pos)
            
        else:
            new_annotation = GeneAnnotation.create(db_id)
            new_annotation.add_mention(original_text, start_pos, end_pos)
            self._gene_annotations.append(new_annotation)
            
        return self.save()
        
    def create_or_update_disease_annotation(self, original_text, db_id, start_pos, end_pos):
        existing_annotation = None
        for annotation in self._disease_annotations:
            if annotation.db_id == db_id:
                existing_annotation = annotation
                break
            
        if existing_annotation:
            existing_annotation.add_mention(original_text, start_pos, end_pos)
            
        else:
            new_annotation = DiseaseAnnotation.create(db_id)
            new_annotation.add_mention(original_text, start_pos, end_pos)
            self._disease_annotations.append(new_annotation)
            
        return self.save()
    
    @classmethod
    def db_to_class(cls, record):
        """ This must be implemented """
        _class = cls(record.get("PMID"), record.get("USERNAME"))
        raw_annotations = record.get("ANNOTATIONS")
        print "Inside annotation db_to_class"
        if "GENE" in raw_annotations:
            print "inside gene annotation"
            raw_annotation = raw_annotations["GENE"]
            hgnc_genes = Hgnc.lookup_by_entrez_id(raw_annotation.keys())
            for hgnc_gene in hgnc_genes:
                mentions = raw_annotation.get(hgnc_gene.entrez_id).get("MENTIONS")
                annotation = GeneAnnotation( hgnc_gene.entrez_id, Annotation.USER)
                annotation.normalized_text = hgnc_gene.symbol
                for mention in mentions:
                    annotation.add_mention(mention.get("TEXT"), mention.get("START_POS"), mention.get("END_POS"))
                    
                _class._gene_annotations.append(annotation)
                
        if "DISEASE" in raw_annotations:
            print "inside disease annotations"
            raw_annotation = raw_annotations["DISEASE"]
            medic_diseases = Medic.get_all_by_fks([key[5:] for key in raw_annotation.keys()])
            print "length is: " + str(len(medic_diseases))
            for medic_disease in medic_diseases:
                mentions = raw_annotation.get(medic_disease.get_disease_id()).get("MENTIONS")
                annotation = DiseaseAnnotation(medic_disease.get_disease_id(), Annotation.USER)
                annotation.normalized_text = medic_disease.get_disease_name()
                for mention in mentions:
                    annotation.add_mention(mention.get("TEXT"), mention.get("START_POS"), mention.get("END_POS"))
                _class._disease_annotations.append(annotation)
                
        return _class
        
    def class_to_db(self):
        """ This must be implemented """
        bson = {}
        if self._id:
            bson["_id"] = self._id
        bson["USERNAME"] = self._username
        bson["PMID"] = self._pmid
        bson["ANNOTATIONS"] = {}
        
        if (len(self._gene_annotations) > 0):
            bson["ANNOTATIONS"]["GENE"] = {}
            for annotation in self._gene_annotations:
                bson["ANNOTATIONS"]["GENE"][annotation.get_db_id()] = annotation.getJson()
                
        if (len(self._disease_annotations) > 0):
            bson["ANNOTATIONS"]["DISEASE"] = {}
            for annotation in self._disease_annotations:
                bson["ANNOTATIONS"]["DISEASE"][annotation.get_db_id()] = annotation.getJson()
                
        return bson
                
    @classmethod
    def get_by_pmid(cls, pmid):
        username = cherrypy.request.login
        obj = cls.get_by_fk( (pmid, username) ) or cls(pmid, username)
        return obj
    
class NlpAnnotations():
    
    COLLECTION = "ANNOTATIONS"
    FK = "PMID"
    
    def __init__(self, pmid):
        self._pmid = pmid
        self._gene_annotations = []
        self._disease_annotations = []
        
    def set_gene_annotations(self, annotations):
        self._gene_annotations = annotations
        
    def get_gene_annotations(self):
        return self._gene_annotations
    
    def set_disease_annotations(self, annotations):
        self._disease_annotations = annotations
        
    def get_disease_annotations(self):
        return self._disease_annotations
    
class Annotation():
    '''
    classdocs
    '''
    SYSTEM = "SYSTEM"
    USER = "USER"

    def __init__(self, db_id, _type):
        '''
        Constructor
        '''
        #self.original_text = original_text if type(original_text) is ListType else [str(original_text)]
        self.normalized_text = None
        self.db_id = db_id
        self.db_name = None
        self._type = _type
        self.meta_data = {"MENTIONS" : [] }
        
    def get_normalized_text(self):
        return self.normalized_text
    
    def get_db_id(self):
        return self.db_id
    
    def get_type(self):
        return self._type
    
    def add_mention(self, text, start_pos, end_pos):
        self.meta_data["MENTIONS"].append({"TEXT" : text, "START_POS" : start_pos, "END_POS" : end_pos})
    
    def getJson(self):
        # DB_ID is not required in this JSON since this value will be persisted as DB_ID : jsonobj
        jsonobj = { }
        jsonobj["MENTIONS"] = self.meta_data.get("MENTIONS")
        jsonobj["NORMALIZED"] = self.normalized_text
        jsonobj["TYPE"] = self._type
        return jsonobj
        
class GeneAnnotation(Annotation):
    
    def __init__(self, db_id, _type = Annotation.SYSTEM):
        Annotation.__init__(self, db_id, _type)
        self.db_name = "HGNC"
        
    @classmethod
    def create(cls, db_id):
        hgnc_gene = Hgnc.lookup_by_entrez_id(db_id)
        if hgnc_gene:
            annotation = cls(db_id, Annotation.USER)
            annotation.normalized_text = hgnc_gene.symbol
            return annotation
            
        else:
            return None
        
    @staticmethod
    def get_from_pubmed(pubmed):
        annotations = []
        raw_annotation = pubmed.get_gene_annotations()
        if raw_annotation:
            hgnc_genes = Hgnc.lookup_by_entrez_id(raw_annotation.keys())
            for hgnc_gene in hgnc_genes:
                original_text = raw_annotation.get(hgnc_gene.entrez_id).get("MENTIONS")
                annotation = GeneAnnotation(hgnc_gene.entrez_id)
                annotation.add_mention(original_text, 0, 0)
                annotations.append(annotation)
            
        return annotations if len(annotations) > 0 else None
    
class DiseaseAnnotation(Annotation):
    
    def __init__(self, db_id, _type = Annotation.SYSTEM):
        Annotation.__init__(self, db_id, _type)
        
    @classmethod
    def create(cls, db_id):
        medic_disease = Medic.lookup_by_dbid(db_id)
        if medic_disease:
            annotation = cls(db_id, Annotation.USER)
            annotation.normalized_text = medic_disease.get_disease_name()
            print annotation
            return annotation
            
        else:
            return None    
       
    @staticmethod
    def get_from_pubmed(pubmed):
        annotations = []
        raw_annotation = pubmed.get_disease_annotations()
        if raw_annotation:
            medic_diseases = Medic.get_all_by_fks([key[5:] for key in raw_annotation.keys()])
            for medic_disease in medic_diseases:
                original_text = raw_annotation.get(medic_disease.get_disease_id()).get("MENTIONS")
                annotation = DiseaseAnnotation(medic_disease.get_disease_id())
                annotation.add_mention(original_text, 0, 0)
                annotations.append(annotation)
                
        return annotations if len(annotations) > 0 else None
        
    