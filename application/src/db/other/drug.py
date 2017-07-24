'''
Created on May 21, 2014

@author: varun
'''

from config import get_db_connection


class Drug(object):
    '''
    classdocs
    '''
    TABLE = "DRUGS"
    
    def __init__(self):
        '''
        Constructor
        '''
        self.brands = []
        self.cas_number = ""
        self.categories = []
        self.ids = {}
        self.groups = []
        self.name = ""
        self.syns = []
        self.type = ""
        
    @staticmethod
    def lookup_by_name(term):
        db = get_db_connection()
        entries = db["DRUGS"].find({"NAME":{"$regex":term, "$options":"i"}})
        drugs = []
        
        for entry in entries:
            drug = Drug()
            drug.brands = entry["BRANDS"]
            drug.cas_number = entry["CAS_NUMBER"]
            drug.categories = entry["CATEGORIES"]
            drug.ids["DRUGBANK"] = entry["DB_ID"]
            drug.groups = entry["GROUPS"]
            drug.name = entry["NAME"]
            drug.syns = entry["SYNS"]
            drug.type = entry["TYPE"]
            drugs.append(drug)
            
        return drugs
    
    @staticmethod
    def search_drug_names(term):
        db = get_db_connection()
        entries = db["DRUGS"].find({"$or":[{"NAME":{"$regex":term, "$options":"i"}}, {"BRANDS":{"$regex": term, "$options":"$i"}} ]})
        drugs = []
        
        for entry in entries:
            drug = Drug()
            drug.brands = entry["BRANDS"]
            drug.cas_number = entry["CAS_NUMBER"]
            drug.categories = entry["CATEGORIES"]
            drug.ids["DRUGBANK"] = entry["DB_ID"]
            drug.groups = entry["GROUPS"]
            drug.name = entry["NAME"]
            drug.syns = entry["SYNS"]
            drug.type = entry["TYPE"]
            drugs.append(drug)
            
        return drugs
        