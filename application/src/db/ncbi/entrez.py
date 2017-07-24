'''
Created on Mar 28, 2014

@author: varun
'''
import re

from Bio import Entrez
import nltk.data


class ICBIEntrez():
    
    ENTREZ_DB = ""
    TIMEOUT = 10
    Entrez.email = "vs454@georgetown.edu"
    
    def __init__(self, entrez_id):
        self.entrez_id = entrez_id
        
    @classmethod
    def fetch(cls, entrez_ids, **kwargs):
        try:
            handle = Entrez.efetch(db = cls.ENTREZ_DB, id = entrez_ids, **kwargs)
        except:
            return None
        
        return handle
    
    def get_mesh_terms(self):      
        handle = Entrez.esearch(db="mesh", term="trastuzumab")
        record = Entrez.read(handle)
        return record["IdList"]
    
    @classmethod
    def search(cls, search_terms, **keywords):
        handle = Entrez.esearch(db = cls.ENTREZ_DB, term = search_terms, **keywords)
        record = Entrez.read(handle, True)
        print "Searched Entrez... Id list length is: "+str(len(record["IdList"]))
        return record 
                
    def get_gene_annotations(self, text):
        gene_syms = self.get_gene_mentions()
        genes = "|".join(["{}".format(sym) for sym in gene_syms])
        print "genes are: "+genes
        regexs = []
        regexs.append("[\(]?(?:"+genes+")[\)]?[-/\s]?(?:negative|positive|express|overexpress|underexpress|amplif|coamplif|aberrat|delet)(?:ing|ion|ied|ication)?[s]?")
        regexs.append("[\w]+[-]level[\s]+(?:"+genes+")")
        print regexs
        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        sentences = sent_detector.tokenize(text)
        #print sentences
        matched = set()
        for sentence in sentences:
            print "sentence is : {}".format(sentence)
            for regex in regexs:
                if re.search(regex, sentence): 
                    matches = re.findall(regex, sentence)
                    for match in matches:
                        print "match is: "+",".join(match)
                    matched.update(matches)
                    print "\tMatches: {}".format(matches)
            
        return matched
    
    def get_gene_mentions(self):
        return None