'''
Created on Sep 10, 2014

@author: varun
'''

from nlp.annotations import GeneAnnotation
from db.ncbi.pubmed import Pubmed

if __name__ == '__main__':
    record = {"1956": {"MENTIONS" : ["epidermal growth factor receptor","ErbB1"]}}
    pubmed = Pubmed.get_publication_from_pmid('23816960')
    annotation = GeneAnnotation.get_from_pubmed(pubmed)
    print annotation