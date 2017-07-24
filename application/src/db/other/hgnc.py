'''
Created on Apr 30, 2014

@author: varun
'''
from __future__ import division
import re
import difflib
import cherrypy
from data.database import DBObject


class Hgnc(DBObject):
    '''
    classdocs
    '''
    COLLECTION = "HGNC"
    FK = "UNIPROT_ID"

    def __init__(self, hgnc_id = None, hgnc_symbol = None, name = None, synonyms = None, chromosome = None, uniprot_id = None, entrez_id = None):
        '''
        Constructor
        '''
        DBObject.__init__(self, None)
        self._id = hgnc_id
        self.symbol = hgnc_symbol
        self.name = name
        self.synonyms = synonyms
        self.chromosome = chromosome
        self.uniprot_id = uniprot_id
        self.entrez_id = entrez_id
        
    def get_similarity(self, to_compare):
        if re.match(to_compare, self.symbol.lower()):
            return (self.symbol, len(re.match(to_compare, self.symbol.lower()).group())/len(self.symbol.lower()))
        
        elif True in [x.startswith(to_compare.lower()) for x in self.synonyms]:
            max_match_str = ""
            max_match_len = 0
            for x in self.synonyms:
                match = re.match(to_compare, x)
                if match and (len(match.group()) > max_match_len):
                    max_match_len = len(match.group())
                    max_match_str = x
                    
            return (max_match_str, len(re.match(to_compare, max_match_str).group())/len(max_match_str))
        
        else:
            matcher = difflib.SequenceMatcher()
            matcher.set_seqs(to_compare, self.name)
            ratio = matcher.ratio()
            #if ratio > 0.5:
            return (self.name, ratio)
            
        return (None, 0.0)
        
    @classmethod
    def db_to_class(cls, record):
        """ This must be implemented """
        hgnc = Hgnc(record.get("_id"), record.get("SYMBOL"), record.get("NAME"), record.get("SYNS"), re.split("[pPqQ]",record.get("CHR"))[0],
                    record.get("UNIPROT_ID"), record.get("ENTREZ_ID"))
        
        return hgnc
        
    def class_to_db(self):
        """ This must be implemented """
    
    @classmethod
    def lookup_by_uniprot_id(cls, uniprot_id):
        return cls.get_by_fk(uniprot_id)
    
    @classmethod
    def search(cls, term):
        results = []
        if len(term.strip()) > 1:
            search_dict = {"$or":[{"SYNS":{ "$regex":"^"+term, "$options":"i" }}, {"SYMBOL":{ "$regex":"^"+term, "$options":"i" } }, {"NAME":{ "$regex":term, "$options":"i" } }]}
            matches_from_db = cls.dbfind(search_dict)
            for match in matches_from_db:
                similarity = match.get_similarity(term)
                if similarity[0]:
                    results.append({"match" : match, "close_match" : similarity[0], "score" : similarity[1]})
                
            results.sort(key = lambda x: x["score"], reverse=True)
            results = results[0:9]
            
            cherrypy.log("Returning 10 results from gene search: "+str(results))
        
        return results
    
    @classmethod
    def lookup_by_symbol(cls, symbol):
        return cls.get_by_field("SYMBOL", symbol)
        
    @classmethod
    def lookup_by_id(cls, hgnc_id):
        return cls.get_by_id(hgnc_id)

    @classmethod
    def lookup_by_entrez_id(cls, entrez_id):
        return cls.get_by_field("ENTREZ_ID", entrez_id) 
    
        