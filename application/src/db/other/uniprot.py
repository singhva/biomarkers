'''
Created on Apr 29, 2014

@author: varun
'''
import urllib2

import pyxb

from config import get_db_connection
from db.other.schema.uniprot_org import uniprot
import pyxb.utils.domutils as domutils


class Uniprot(object):
    '''
    classdocs
    '''
    base_url = "http://www.uniprot.org"

    def __init__(self, uniprot_id = None):
        '''
        Constructor
        '''
        self._id = uniprot_id
        self.name = None
        self.protein_name = None
        self.alt_names = None
        if not self.__fetch_from_db__():
            self.__fetch_from_web__()
        
    def __fetch_from_web__(self):
        try:
            response = urllib2.urlopen(Uniprot.base_url+"/uniprot/"+self._id+".xml").read()
            doc = domutils.StringToDOM(response)
            pyxb.RequireValidWhenParsing(False)
            self.uniprot = uniprot.createFromDOM(doc.documentElement)
            self.name = self.uniprot.entry[0].protein.recommendedName.fullName.value()
        except:
            print "Caught exception"
        
    def __fetch_from_db__(self):
        db = get_db_connection()
        entry = db["UNIPROT"].find_one({"_id": self._id})
        if entry is None:
            return
        else:
            self.name = entry["ENTRY_NAME"]
            return True
    
    def get_name(self):
        return self.name
    
    def get_alt_names(self):
        names = []
        for alt in self.uniprot.entry[0].protein.alternativeName:
            names.append(alt.fullName.value())
        
        return names
    
    def get_gene_symbol(self):
        return self.uniprot.entry[0].gene[0].name[0].value()
