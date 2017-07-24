'''
Created on Aug 13, 2014

@author: varun
'''
import re
import difflib
import cherrypy
from data.database import DBObject


class Medic(DBObject):
    
    COLLECTION = "MEDIC"
    FK = "DB_ID"
    
    def __init__(self, db_record = None):
        DBObject.__init__(self, db_record)
        self._disease_name = None
        self._alt_disease_ids = None
        self._definition = None
        self._parent_ids = None
        self._synonyms = None
        
        
    def get_disease_id(self):
        fk = self.get_fk()
        if fk.isdigit():
            return "OMIM:"+str(fk)
        else:
            return "MESH:"+str(fk)
        #return self.get_fk()
    
    def set_disease_id(self, disease_id):
        self._fk = disease_id
    
    def get_disease_name(self):
        return self._disease_name
    
    def set_disease_name(self, name):
        self._disease_name = name
    
    def get_alt_disease_ids(self):
        return self._alt_disease_ids
    
    def set_alt_disease_ids(self, alt_ids):
        self._alt_disease_ids = alt_ids
    
    def get_disease_definition(self):
        return self._definition
    
    def set_disease_definition(self, definition):
        self._definition = definition
    
    def get_parent_ids(self):
        return self._parent_ids
    
    def set_parent_ids(self, parent_ids):
        self._parent_ids = parent_ids
    
    def get_disease_synonyms(self):
        return self._synonyms
    
    def set_disease_synonyms(self, synonyms):
        self._synonyms = synonyms
    
    @classmethod
    def db_to_class(cls, db_record):
        medic = Medic(db_record)
        medic._disease_name = db_record.get("NAME")
        medic._alt_disease_ids = db_record.get("ALT_IDS")
        medic._definition = db_record.get("DEFINITION")
        medic._parent_ids = db_record.get("PARENT_IDS")
        medic._synonyms = db_record.get("SYNS")
        
        return medic
        
    def class_to_db(self):
        bson = {}
        if self._id:
            bson["_id"] = self._id
            
        bson["DB_ID"] = self.get_disease_id()
        bson["NAME"] = self.get_disease_name()
        bson["ALT_IDS"] = self.get_alt_disease_ids() or []
        bson["DEFINITION"] = self.get_disease_definition()
        bson["PARENT_IDS"] = self.get_parent_ids()
        bson["SYNS"] = self.get_disease_synonyms() or []
        
        return bson
    
    @classmethod
    def lookup_by_dbid(cls, db_id):
        if (re.search(":", db_id)):
            db_id = db_id.split(":")[1]
        return cls.get_by_fk(db_id)
    
    def get_similarity(self, to_compare):
        if re.match(to_compare, self.get_disease_name().lower()):
            return (self.get_disease_name(), len(re.match(to_compare, self.get_disease_name().lower()).group())/len(self.get_disease_name().lower()))
        
        elif True in [x.startswith(to_compare.lower()) for x in self.get_disease_synonyms()]:
            max_match_str = ""
            max_match_len = 0
            for x in self.get_disease_synonyms:
                match = re.match(to_compare, x)
                if match and (len(match.group()) > max_match_len):
                    max_match_len = len(match.group())
                    max_match_str = x
                    
            return (max_match_str, len(re.match(to_compare, max_match_str).group())/len(max_match_str))
        
        else:
            matcher = difflib.SequenceMatcher()
            matcher.set_seqs(to_compare, self.get_disease_name())
            ratio = matcher.ratio()
            #if ratio > 0.5:
            return (self.get_disease_name(), ratio)
    
    @classmethod
    def search(cls, term):
        results = []
        if len(term.strip()) > 1:
            search_dict = {"$or":[{"SYNS":{ "$regex":"^"+term, "$options":"i" }}, {"NAME":{ "$regex":term, "$options":"i" } }]}
            matches_from_db = cls.dbfind(search_dict)
            for match in matches_from_db:
                similarity = match.get_similarity(term)
                if similarity[0]:
                    results.append({"match" : match, "close_match" : similarity[0], "score" : similarity[1]})
                
            results.sort(key = lambda x: x["score"], reverse=True)
            results = results[0:9]
            
            cherrypy.log("Returning 10 results from disease search: "+str(results))
        
        return results
    
    
if __name__ == '__main__':
    fk_list = [u'D016609', u'D001943', u'D001924']
    medic = Medic.get_all_by_fks(fk_list)
    for m in medic:
        print m.get_disease_name()
        