'''
Created on Apr 8, 2014

@author: varun
'''
import os
from datetime import datetime
import json
import pickle
import re
import urllib2
import codecs
import pprint
from types import *

from Bio import Entrez, Medline
from nltk.parse.stanford import StanfordParser
from nltk.tree import Tree
from nltk.probability import FreqDist
import nltk

from misc import utils
from db.ncbi.clinicaltrials import ClinicalStudy
from db.ncbi.pubmed import Pubmed
from data.process_pdf import PdfReader
from nlp.genia_chunker import GeniaChunker
from nlp.evidence import Evidence

base_dir = "/Users/varun/Documents/papers/NLP/"

def main():
    #save_pubmed_search('(her2[All Fields] AND positive[All Fields]) AND Clinical Trial[ptyp] AND (hasabstract[text] AND "2004/04/11"[PDat] : "2014/04/08"[PDat] AND "humans"[MeSH Terms] AND jsubsetaim[text])', \
    #'her2_positive_ct_10years_humans_core.pickle')
    #pubmeds = get_saved_pubmed_search("her2_positive_ct_10years_humans_core.pickle")
    pubmed = Pubmed.get_publication_from_pmid("26379080")  #16014882, 15972865
    print pubmed.get_mesh_terms()
    if pubmed.download_pdf(base_dir):
        pdf = pubmed.get_pdf()
    #    print "\n".join(pdf.sections[PdfReader.MM]["text"])
    #annotations = pubmed.get_annotations()
    #print annotations
    #ids = Pubmed.search('(her2) AND Clinical Trial[ptyp] AND clinicaltrials.gov [si] AND ("2004/06/01"[PDat] : "2014/05/30"[PDat] AND "humans"[MeSH Terms]', sort='pub date')
    #print str(ids)
    #pubmeds = pubmed.get_publications_from_ids(['24846037', '24501009'])
    publications = pubmed.search("HER2 trastuzumab")
    for publication in publications:
        print publication.get_pmid()
    print len(publications)
    #pubmed._has_fulltext = True
    #trial_ids = pubmed.get_clinical_trial_ids()
    #cs = ClinicalStudy.get("NCT01428414")
    #print cs.get_enrolled_patients_count()
    #print cs.get_patient_demographics()
    #analyze_case_control_articles()
    #analyze_clinical_trials()
    #analyze_rct_articles()
    #analyze_paraffin_articles()
    #analyze_review_articles()
    #analyze_expression_titles()
    #evidence = Evidence(20467918)
    #evidence.find_level()
    #chunking(pubmed)
    #chunker = GeniaChunker()
    #chunker.read()
    #chunker.train()
    #chunker.load()
    sentence = '''
    Intratumoural hENT1 and RRM1 expression levels were investigated immunohistochemically in 127 patients with advanced cholangiocarcinoma 
    who underwent surgical resection (68 with AGC and 59 without AGC). The impacts of hENT1 and RRM1 expression on survival were evaluated.
    '''
    #chunker.parse(sentence)
    
def analyze_clinical_trials():
    ids = Pubmed.search('RRM1[Title/Abstract]', retmax=200)["IdList"]
    pubmeds = Pubmed.get_publications_from_pmids(ids, False)
    post_hoc_re = re.compile(r"paraffin[\s-]?embedded|embedded")
    count = 0
    for pubmed in pubmeds:
        print "\n------------------------------------------------------------\n"
        print "Pubmed ID: " + pubmed.get_pmid()
        match = post_hoc_re.search(pubmed.get_abstract())
        if match:
            count += 1
            index = match.start()
            print "Match from abstract: ",
            print " ".join(pubmed.get_abstract()[0:index].split()[-3:]) + " " + match.group(0) 
            if pubmed.download_pdf(base_dir):
                pdf_file = pubmed.get_pdf(base_dir)
                pdf = PdfReader(pdf_file)
                pdf.parse()
                mm = pdf.sections[PdfReader.MM]["text"]
                mm = "\n".join(mm[:20])
                match = post_hoc_re.search(mm)
                if match:
                    print "Match from MM section: ",
                    index = match.start()
                    print " ".join(mm[0:index].split()[-3:]) + " " + match.group(0)
            
    print "Count is %d" % count
    
def chunking(pubmed):
    base_dir = "/Users/varun/Documents/papers/NLP/"
    if pubmed.download_pdf(base_dir):
        pdf_file = pubmed.get_pdf(base_dir)
        pdf = PdfReader(pdf_file)
        pdf.parse()
        
        mm = pdf.sections[PdfReader.MM]["text"]
        sentences = nltk.sent_tokenize(pubmed.get_abstract())
        words = [nltk.word_tokenize(sent) for sent in sentences]
        pos_tags = [nltk.pos_tag(word) for word in words]
        print pos_tags
                
        grammar = r"""
            CHUNK: {<PRP><RB>?<VBD><JJ|CD>?<NN.*>}
                    {<CC><VBD><RB><VBN>}
                    {<NN.*><IN><.*>+<VB>}
                    {<CD><NNS>}
        """
        cp = nltk.RegexpParser(grammar)
        '''
        cp = StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz",
                            path_to_jar="/Users/varun/.m2/repository/edu/stanford/nlp/stanford-parser/3.5.2/stanford-parser-3.5.2.jar",
                            path_to_models_jar="/Users/varun/.m2/repository/edu/stanford/nlp/stanford-parser/3.5.2/stanford-parser-3.5.2-models.jar")
        '''
        #list_of_nps = []
        for pos in pos_tags:
        #for sentence in sentences[:1]:
            tree = cp.parse(pos)
            #list_of_nps = ExtractPhrases(tree, "NP")
            for subtree in tree.subtrees():
                if subtree.label() == "CHUNK": print " ".join(nltk.tag.untag(subtree))
                #print subtree
                #if subtree.label() == "NP": print subtree
                
        #print list_of_nps
                
def analyze_case_control_articles():
    #ids = Pubmed.search('NSCLC AND "case control"', retmax=100)["IdList"]
    ids = ['16014882']
    base_dir = "/Users/varun/Documents/papers/NLP/"
    pubmeds = Pubmed.get_publications_from_pmids(ids, False)
    case_control_re = re.compile("case|control|case-control", re.IGNORECASE)
    patients_re = re.compile("[pP]atients|[mM]en|[wW]omen")
    grammar = r"""
        CHUNK: {<CD><.*>*<NNS>}
    """
    cp = nltk.RegexpParser(grammar)
    for pubmed in pubmeds:
        print "\n------------------------------------------------------------\n"
        print "Pubmed ID: " + pubmed.get_pmid()
        if pubmed.download_pdf(base_dir):
            pdf_file = pubmed.get_pdf(base_dir)
            pdf = PdfReader(pdf_file)
            pdf.parse()
            text = pdf.sections[PdfReader.RESULTS]["text"]
            text = "\n".join(text[:10])
        else:
            text = pubmed.get_abstract()
        if case_control_re.search(text):
            sentences = nltk.sent_tokenize(text)
            for sentence in sentences:
                if case_control_re.search(sentence):
                    #print sentence
                    tree = cp.parse(nltk.pos_tag(nltk.word_tokenize(sentence)) )
                    for subtree in tree.subtrees():
                        if subtree.label() == "CHUNK": 
                            print " ".join(nltk.tag.untag(subtree))
                            print list(subtree)[0]
                    
    
def analyze_meta_analysis_articles():
    ids = Pubmed.search('Meta-Analysis[Publication Type] AND NSCLC', retmax=100)["IdList"]
    #ids = ['25360721']
    pubmeds = Pubmed.get_publications_from_pmids(ids, False)
    meta_analysis_re = re.compile("meta[-]?analysis", re.IGNORECASE)
    study_re = re.compile("[sS]tudies|[tT]rials|RCT[s]?|prospective randomized trials|randomized trials|articles|papers|clinical studies")
    include_re = re.compile("[iI]ncluded|[iI]dentified|analyzed|enrolled|performed|published")
    patients_re = re.compile("[pP]atients|[mM]en|[wW]omen")
    base_dir = "/Users/varun/Documents/papers/NLP"
    grammar = r"""
        CHUNK: {<CD><JJ.*>?<NN.*>}
    """
    cp = nltk.RegexpParser(grammar)
    count = 0
    for pubmed in pubmeds:
        print "\n------------------------------------------------------------\n"
        print "Pubmed ID: " + pubmed.get_pmid()
        abstract = pubmed.get_abstract()
        sentences = nltk.sent_tokenize(abstract)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            if study_re.search(sentence):# and include_re.search(sentence):
                pos_tags = nltk.pos_tag(words)
                tree = cp.parse(pos_tags)
                chunk_found = False
                for subtree in tree.subtrees():
                    if subtree.node == "CHUNK" and study_re.search(" ".join(nltk.tag.untag(subtree))): 
                        #print " ".join(nltk.tag.untag(subtree))
                        #count += 1
                        chunk_found = True
                chunk_found &= len([pos for (word, pos) in pos_tags if word.endswith("ed") and pos.startswith("VB")]) > 0
                if chunk_found: 
                    count += 1
                    print sentence

                '''
                index = [word.lower() for word in words].index("studies")
                low = 0 if (index <=5 ) else (index - 5)
                high = index + 5
                print " ".join(words[low : high])
                '''        
    print "\n\n"
    print "Number of studies: %d" % count


def analyze_rct_articles():
    ids = Pubmed.search('RRM1[Title/Abstract]', retmax=100)["IdList"]
    pubmeds = Pubmed.get_publications_from_pmids(ids, False)
    randomized_re = re.compile(r"[rR]andomized|[rR]andomised")
    count = 0
    for pubmed in pubmeds:
        print "\n------------------------------------------------------------\n"
        print "Pubmed ID: " + pubmed.get_pmid()
        evidence = Evidence(pubmed)
        meta_data_based = ("Randomized Controlled Trial" in (pubmed.get_publication_types() or [])) or ("randomized controlled trials" in (pubmed.get_mesh_terms() or []))
        if meta_data_based:
            print "Randomized based on Meta Data"
            
        #evidence_based = (randomized_re.search(pubmed.get_title()) or randomized_re.search(pubmed.get_abstract())) is not None
        evidence_based = evidence.is_randomized()
        if evidence_based:
            print "Randomized based on text"
            
        if (meta_data_based ^ evidence_based): count += 1
        
    print "Count is: %d" %count
    
def analyze_review_articles():
    ids = Pubmed.search('BRCA1[Title/Abstract] AND Review[Publication Type] ', retmax=100)["IdList"]
    pubmeds = Pubmed.get_publications_from_pmids(ids, False)
    review_re = re.compile(r"\breview[s]?\b|\breviewed\b|overview|summarize[d]?\b|summarise[d]?\b|analyzed|comprehensive|literature")
    for pubmed in pubmeds:
        print "\n------------------------------------------------------------\n"
        print "Pubmed ID: " + pubmed.get_pmid()
        text = pubmed.get_title() + "\n" + pubmed.get_abstract()
        match = review_re.search(text)
        if match:
            index = match.start()
            print " ".join(text[0:index].split()[-3:]) + " " + match.group(0)
            
def analyze_paraffin_articles():
    ids = Pubmed.search('RRM1[Title/Abstract] AND paraffin[Title/Abstract] ', retmax=100)["IdList"]
    pubmeds = Pubmed.get_publications_from_pmids(ids, False)
    review_re = re.compile(r"paraffin", re.IGNORECASE)
    for pubmed in pubmeds:
        print "\n------------------------------------------------------------\n"
        print "Pubmed ID: " + pubmed.get_pmid()
        text = pubmed.get_title() + "\n" + pubmed.get_abstract()
        match = review_re.search(text)
        if match:
            start = match.start()
            end = match.end()
            #print " ".join(text[0:start].split()[-5:]) + " " + match.group(0) + " " + " ".join(text[end + 1:].split()[:5])
            sentences = nltk.sent_tokenize(text)
            for sent in sentences:
                match2 = review_re.search(sent)
                if match2:
                    print sent                    
             
def find_pubmed_meta_analysis_articles():
    ids = Pubmed.search('Meta-Analysis[Publication Type] AND NSCLC', retmax=1500)["IdList"]
    pubmeds = Pubmed.get_publications_from_pmids(ids, False)
    meta_analysis_re = re.compile("meta|meta[-]?analysis", re.IGNORECASE)
    meta_analysis_ids = []
    non_meta_analysis_pubs = []
    journals = set()
    for pubmed in pubmeds:
        types = pubmed.get_publication_types()
        if pubmed.get_abstract() != "" and pubmed.get_abstract() is not None and meta_analysis_re.search(pubmed.get_abstract()): 
            meta_analysis_ids.append(pubmed.get_pmid())
        else:
            non_meta_analysis_pubs.append(pubmed)
            journals.add(pubmed.get_journal())
            print "Pubmed: " + pubmed.get_pmid() + ", journal: " + pubmed.get_journal()
            
    print len(meta_analysis_ids)
    print len(non_meta_analysis_pubs)
    print pprint.pprint(journals)
    
    non_downloadable = []
    
    for pubmed in non_meta_analysis_pubs:
        if not pubmed.download_pdf("/Users/varun/Documents/papers/NLP/"):
            print "Not downloaded: " + pubmed.get_pmid()
            non_downloadable.append(pubmed)
            
        else:
            print "downloaded: " + pubmed.get_pmid()
        print ""    
        
    print "Unable to download " + str(len(non_downloadable)) + " articles out of " + str(len(non_meta_analysis_pubs))
            
def save_pubmed_search(search_term, file_name):
    Entrez.email = "vs454@georgetown.edu"
    handle = Entrez.esearch(db="pubmed", term = search_term, retmax = 100000)
    record = Entrez.read(handle, True)
    ids = record["IdList"]
    print ids
    
    handle = Entrez.efetch(db="pubmed",id = ",".join(ids), rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)
    f = open("/Users/varun/Desktop/Cancer_Biomarkers/pubmed/"+file_name, "w")
    pickle.dump(records, f)
    f.close()
    
def get_saved_pubmed_search(file_name):
    records = pickle.load(open("/Users/varun/Desktop/Cancer_Biomarkers/pubmed/"+file_name))
    pubmeds = []
    for record in records:
        pubmed = Pubmed(record.get("PMID"))
        pubmed.record = record
        pubmeds.append(pubmed)
        
    return pubmeds

if __name__ == '__main__':
    main()