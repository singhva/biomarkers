'''
Created on Aug 22, 2014

@author: varun
'''

from collections import OrderedDict

from db.ncbi.pubmed import Pubmed
from misc import utils
from config import get_cache_connection
from nlp.annotations import GeneAnnotation, DiseaseAnnotation, Annotation

MAX_EXPIRE_DURATION = 360
MAX_PER_PAGE = 10

class PubmedService(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def lookup_cache_key(self, cache_key, start_index, end_index):
        cache = get_cache_connection()
        ids = cache.lrange(cache_key, start_index, end_index)
        publications = Pubmed.get_publications_from_pmids(ids)
        
        return publications
    
    def process_results_from_cache(self, cache_key, pagenum):
        cache = get_cache_connection()
        count = cache.llen(cache_key)
        pages = count / MAX_PER_PAGE + (1 if (count % MAX_PER_PAGE) > 0 else 0)
        
        start_index, end_index = self.get_start_end_indexes(pagenum, pages, count)

        results = self.lookup_cache_key(cache_key, start_index, end_index)
        jsonobj = self.processPublications(results, count, pagenum)
        
        return jsonobj
    
    def cache_session_publication_ids(self, cache_key, pubmeds):
        cache = get_cache_connection()
        if pubmeds and len(pubmeds) > 0:
            cache.rpush(cache_key, *[pubmed.entrez_id for pubmed in pubmeds])
        
    def cache_global_search_publication_ids(self, cache_key, pubmeds):
        cache = get_cache_connection()
        if pubmeds and len(pubmeds) > 0:
            cache.rpush(cache_key, *[pubmed.entrez_id for pubmed in pubmeds])
            cache.expire(cache_key, MAX_EXPIRE_DURATION)
    
    def get_page_num(self, move, current_page_num):
        pagenum = 1
        
        if move == "first":
            pagenum = 1
        
        elif move == "previous":
            pagenum = max((current_page_num - 1), 1)
            
        elif move == "next":
            pagenum = current_page_num + 1
            
        elif move == "last":
            pagenum = -1
            
        else:
            pagenum = 1
        
        return pagenum
    
    def get_start_end_indexes(self, pagenum, pages, count):
        start_index = 0
        
        if pagenum == -1:
            start_index = (pages - 1) * MAX_PER_PAGE
            
        else:
            start_index = (pagenum - 1) * MAX_PER_PAGE
            
        end_index = min(start_index + MAX_PER_PAGE, count) - 1 
        
        return (start_index, end_index)

    def processPublications(self, publications, total_count, pagenum):
        jsonobj = { "publications" : [] }
        total_pages = total_count / MAX_PER_PAGE + (1 if (total_count % MAX_PER_PAGE) > 0 else 0)
        start_index, end_index = self.get_start_end_indexes(pagenum, total_pages, total_count)
        
        jsonobj["count"] = total_count           
        jsonobj["pages"] = total_pages
        jsonobj["pagenum"] = pagenum if pagenum > 0 else total_pages
        jsonobj["start_index"] = start_index + 1
        jsonobj["max_per_page"] = MAX_PER_PAGE
        jsonobj["end_index"] = end_index + 1
        
        print jsonobj
                    
        for publication in publications:
            #annotation = db["ANNOTATIONS"].find_one( {"PMID" : result.get_pmid()} )
            #genes = annotation.get("GENE")
            #diseases = annotation.get("DISEASE")
            #gene_annotations = GeneAnnotation.get_from_pubmed(publication)
            #disease_annotations = DiseaseAnnotation.get_from_pubmed(publication)
            manual_annotations = publication.get_manual_annotations()
            nlp_annotations = publication.get_nlp_annotations()
            gene_annotations = nlp_annotations.get_gene_annotations() + manual_annotations.get_gene_annotations()
            disease_annotations = nlp_annotations.get_disease_annotations() + manual_annotations.get_disease_annotations()
            obj = {
                "pmid":publication.get_pmid(),
                "title":publication.get_title(),
                "date": publication.get_publication_date().strftime("%b, %d %Y"),
                "journal_title":publication.get_journal(),
                "abstract":publication.get_abstract(),
                "trial_info":publication.get_clinical_trial_info()
                }
            
            if gene_annotations:
                obj["biomarkers"] = {}
                obj["biomarkers"][Annotation.USER] = [ annotation.getJson() for annotation in manual_annotations.get_gene_annotations() ]
                obj["biomarkers"][Annotation.SYSTEM] = [ annotation.getJson() for annotation in nlp_annotations.get_gene_annotations() ]
                
            if disease_annotations:
                obj["diseases"] = {}
                obj["diseases"][Annotation.USER] = [ annotation.getJson() for annotation in manual_annotations.get_disease_annotations()]
                obj["diseases"][Annotation.SYSTEM] = [ annotation.getJson() for annotation in nlp_annotations.get_disease_annotations()]
                    
            '''
            if genes:
                hgnc_syms = []
                hgnc_genes = Hgnc.lookup_by_entrez_id(genes.keys())
                for gene in hgnc_genes:
                    hgnc_syms.append(gene.symbol)
                obj["biomarkers"] = hgnc_syms
                    
            if diseases:
                medic_names = []
                names = [name[5:] for name in diseases.keys()]
                for disease in Medic.get_all_by_fks(names):
                    medic_names.append(disease.get_disease_name())                               
                obj["diseases"] = medic_names
            '''
                
            jsonobj["publications"].append(obj)
            
        return jsonobj        
        
    @staticmethod
    def get_interesting_stuff(pmid):
        pubmed = Pubmed.get_publication_from_pmid(pmid)
        #gene_annotations = GeneAnnotation.get_from_pubmed(pubmed)
        #disease_annotations = DiseaseAnnotation.get_from_pubmed(pubmed)   
        manual_annotations = pubmed.get_manual_annotations()
        nlp_annotations = pubmed.get_nlp_annotations()     
        #annotations = Pubmed.get_annotations(pubmed)
        interesting_stuff = {"pmid":pmid, "abstract": pubmed.get_abstract()}
        interesting_stuff["trial_info"] = pubmed.get_clinical_trial_info()
        interesting_stuff["trial_ids"] = pubmed.get_clinical_trial_ids()
        interesting_stuff["publication_types"] = pubmed.get_publication_types()
        #interesting_stuff["marker_status"] = pubmed.get_marker_details(annotations)
        #interesting_stuff["diseases"] = [ annotation.getJson() for annotation in disease_annotations ]
        interesting_stuff["annotations"] = { "genes" : {}, "diseases" : {} }
        interesting_stuff["annotations"]["diseases"][Annotation.USER] = [ annotation.getJson() for annotation in manual_annotations.get_disease_annotations()]
        interesting_stuff["annotations"]["diseases"][Annotation.SYSTEM] = [ annotation.getJson() for annotation in nlp_annotations.get_disease_annotations()]
        
        interesting_stuff["annotations"]["genes"][Annotation.USER] = [ annotation.getJson() for annotation in manual_annotations.get_gene_annotations()]
        interesting_stuff["annotations"]["genes"][Annotation.SYSTEM] = [ annotation.getJson() for annotation in manual_annotations.get_gene_annotations()]
        #interesting_stuff["drugs"] = pubmed.get_drugs(annotations)
        interesting_stuff["patient_demographics"] = pubmed.get_patient_characteristics()
        interesting_stuff["results"] = pubmed.get_results_of_study()
        
        #print "interesting stuff: "+str(interesting_stuff)
        print "Disease annotations: " + str(interesting_stuff["annotations"]["diseases"])
            
        return interesting_stuff
    
    
    def filter(self, pubmeds, filters):
        filtered_pubmed_list = []
                
        if filters:
            print "Inside pubmed filter: "+str(filters)
            filter_map = utils.get_filter_map(filters)      
            for filter_key, filter_value in filter_map.iteritems():                          
                if filter_key == Pubmed.FILTER_KEY_JOURNAL:
                    for pubmed in pubmeds:
                        if (pubmed.get_journal().lower() in filter_value):
                            filtered_pubmed_list.append(pubmed)
                        
            return filtered_pubmed_list
        
        else:
            return pubmeds
        
    def get_filters(self, publications):
        journal_names = {}
        publication_years = {}
        for pubmed in publications:
            journal_name = pubmed.get_journal()
            publication_year = pubmed.get_publication_date().year
            count = journal_names.get(journal_name, 0)
            journal_names[journal_name] = count + 1
            count = publication_years.get(publication_year, 0)
            publication_years[publication_year] = count + 1
            
        sorted_journal_dict = OrderedDict(sorted(journal_names.items(), key = lambda t : t[0]))
        sorted_publication_years = OrderedDict(sorted(publication_years.items(), key = lambda t: t[0]))
        
        return {"journal_names" : sorted_journal_dict, "publication_years" : sorted_publication_years}
        
    def sort(self, pubmeds, sort_by):
        if sort_by and "" != sort_by:
            if sort_by == Pubmed.SORT_KEY_RELEVANCE[0]:
                return self.sort_by_relevance(pubmeds)
            
            elif sort_by == Pubmed.SORT_KEY_JOURNAL[0]:
                return self.sort_by_journal_name(pubmeds)
            
        else:
            return pubmeds
        
    def sort_by_journal_name(self, pubmeds):
        return sorted(pubmeds, key = lambda pubmed: pubmed.get_journal())
    
    def sort_by_relevance(self, pubmeds):
        group1 = []
        group2 = []
        group3 = []
        group4 = []
        
        rest = []
        
        all_groups = []
        for pubmed in pubmeds:
            pubmed.populate_features()
            if pubmed._features['is_clinical_trial_phase3'] and pubmed._features['is_randomized']:
                group1.append(pubmed)
                
            elif pubmed._features['is_clinical_trial_phase3']:
                group2.append(pubmed)
                
            elif pubmed._features['is_clinical_trial_phase2']:
                group3.append(pubmed)
                
            elif pubmed._features['is_clinical_trial_phase1']:
                group4.append(pubmed)
                
            else:
                rest.append(pubmed)

        all_groups.extend(group1)
        all_groups.extend(group2)
        all_groups.extend(group3)
        all_groups.extend(group4)
        all_groups.extend(rest)
        
        return all_groups
    
    
        