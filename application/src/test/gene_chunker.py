'''
Created on Apr 10, 2014

@author: varun
'''

import pickle
import re

import nltk
import nltk.chunk.util

from nlp.gene_chunk_parser import GeneChunker


def main():
    
    '''
    sents = get_training_data()
    training_sents = sents
    f_training_data = open("/Users/varun/Desktop/Cancer_Biomarkers/training.pickle","w")
    pickle.dump(sents, f_training_data)
    f_training_data.close()
    '''
    
    f_training_data = open("/Users/varun/Desktop/Cancer_Biomarkers/training.pickle","r")
    training_sents = pickle.load(f_training_data)
    f_training_data.close()
    
    #training_sent_len = int(len(sents) * 0.8)
    #training_sents = sents[:training_sent_len]
    #test_sents = sents[training_sent_len:-1]
    #test_sents = []
    #test_sents = [(w,t,c) for ((w,t), c) in sent for sent in test_sents]
    #print "test sents: "+str(test_sents)
    chunker = GeneChunker(training_sents)
    print "saving as pickle... ",
    f = open("/Users/varun/Desktop/Cancer_Biomarkers/gene_chunker.pickle", "w")
    pickle.dump(chunker, f)
    f.close()
    print "saved"
    #print chunker.evaluate(nltk.chunk.util.conlltags2tree(test_sents))
    
    '''
    f = open("/Users/varun/Desktop/Cancer_Biomarkers/gene_chunker.pickle")
    chunker = pickle.load(f)
    f.close()
    '''
    sentence = '''
        Expression of the human papillomavirus type 11 E5A protein from the E1E4,E5 transcript.
    '''
    print chunker.parse(nltk.pos_tag(nltk.word_tokenize(sentence)))
    
def get_training_data():
    print "opening genetag file"
    tag_f = open("/Users/varun/Desktop/Cancer_Biomarkers/medtag/genetag/genetag.tag", "r")
    train_sents = []
    for i, line in enumerate(tag_f):
        if(i % 2 == 1):
            if i % 5 == 0: print "line number: "+str(i)
            iob_sentence = []
            untagged_sent = re.sub("_TAG", "", line)
            words = nltk.word_tokenize(untagged_sent)
            tagged_sent = nltk.pos_tag(words)
            for j, tagged_word in enumerate(line.split()):
                #print "tagged word is: "+tagged_word
                word, tag = tagged_word.split("_")
                if tag == "TAG":
                    iob_sentence.append(((word, tagged_sent[j][1]), "O"))
                    prev_tag = "TAG"
                else:
                    iob_tag = "I-NP" if ((tag == prev_tag)) else "B-NP"
                    iob_sentence.append(((word, tagged_sent[j][1]), iob_tag))
                    prev_tag = tag
            #print iob_sentence
            train_sents.append(iob_sentence)
            
    print "closing genetag file"
    tag_f.close()
    return train_sents


if __name__ == '__main__':
    main()