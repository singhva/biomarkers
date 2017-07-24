'''
Created on Apr 7, 2014

@author: varun
'''
import re

import nltk
import nltk.data

from data.utils import Utils
from ncbi import entrez


def main():
    sentence = '''
    Previous studies have demonstrated that ARTEMIN (ARTN) functions as a cancer stem cell (CSC) and metastatic factor in 
    mammary carcinoma. Herein, we report that ARTN mediates acquired resistance to Trastuzumab in HER2 positive mammary 
    carcinoma cells. Ligands which increase HER2 activity increased ARTN expression in HER2 positive mammary carcinoma cells, 
    whereas Trastuzumab inhibited ARTN expression. Forced expression of ARTN decreased the sensitivity of HER2 positive 
    mammary carcinoma cells to Trastuzumab both in in vitro and in vivo. Conversely siRNA mediated depletion of ARTN enhanced 
    Trastuzumab efficacy. Cells with acquired resistance to Trastuzumab exhibited increased ARTN expression, the depletion 
    of which restored Trastuzumab sensitivity. Trastuzumab resistance produced an increased CSC population concomitant with 
    enhanced mammospheric growth. ARTN mediated the enhancement of the CSC population by increased BCL-2 expression and the 
    CSC population in Trastuzumab resistant cells was abrogated upon inhibition of BCL-2. Hence, we conclude that ARTN is one 
    mediator of acquired resistance to Trastuzumab in HER2 positive mammary carcinoma cells.
    '''
    #matches = get_gene_mentions(["TOP2A", "HER2"], sentence)
    #print matches
    Utils.parse_pubmed_abstract(sentence, ["HER2"])

def get_gene_mentions(gene_syms, text):
    genes = "|".join(["{}".format(sym) for sym in gene_syms])
    print "genes are: "+genes
    regexs = []
    regexs.append("[\(]?(?:"+genes+")[\)]?[-/\s]?(?:negative|positive|express|overexpress|underexpress|amplif|coamplif|aberrat|delet)(?:ing|ion|ied|ication)?[s]?")
    regexs.append("[\w]+[-]level[\s]+(?:"+genes+")")
    print regexs
    #expression = "((negative)|(positive)|(overexpress)|(under)|(amplif)(ing|ion|ied)?)"
    #expression = "((negative|positive|overexpress|underexpress|amplif)(ing|ion|ied|ication)?)"
    #regex = gene
    #print "regex is: "+regex
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
        
        #search1 = re.search(gene, sentence)
        #search2 = re.search(expression, sentence)
        #print "entering else"
        #if search1 and search2:
            #print "Substring is: {}, {}, {}".format(search1.start(), search2.start(), sentence[search1.start():search2.end()])
        
    return matched

if __name__ == '__main__':
    main()