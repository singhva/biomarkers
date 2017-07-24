'''
Created on Apr 29, 2014

@author: varun
'''
from external.hgnc import Hgnc
from external.uniprot import Uniprot


def main():
    #uniprot = Uniprot("P04626")
    #print uniprot.get_name()
    #print uniprot.get_gene_symbol()
    #print uniprot.get_alt_names()
    hgnc = Hgnc(uniprot_id="P04626")
    print hgnc.symbol

if __name__ == '__main__':
    main()