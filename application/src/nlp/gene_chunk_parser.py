'''
Created on Apr 10, 2014

@author: varun
'''
import pickle
import re

import nltk
import nltk.chunk
from nltk.classify import SklearnClassifier
from nltk.classify import maxent
from sklearn.naive_bayes import BernoulliNB


class ConsecutiveNPGeneChunkTagger(nltk.TaggerI):
    
    def __init__(self, train_sents):
        train_set = []
        print "initializing chunktagger "
        
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            #print "tagged sent is: "+str(tagged_sent)
            #print "\tuntagged sent is: "+str(untagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                feature_set = self.npchunk_features(untagged_sent, i, history)
                #print "feature set is: "+str(feature_set)
                train_set.append((feature_set, tag))
                history.append(tag)
    
        print "training chunktagger ....",
        self.classifier = maxent.MaxentClassifier.train(train_set, algorithm ='IIS', trace=0)
        #self.classifier = nltk.NaiveBayesClassifier.train(train_set)
        #self.classifier = SklearnClassifier(BernoulliNB()).train(train_set)
        print "done"
        
    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = self.npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)
        
        
    def npchunk_features(self, sentence, i, history):
        word, pos = sentence[i]
        if i == 0:
            prevword, prevpos = "<START>", "<START>"
        else:
            prevword, prevpos = sentence[i-1]
        return {"pos": pos, "word": word, "prevword": prevword, "prevpos":prevpos}


class GeneChunker(nltk.ChunkParserI):
    '''
    classdocs
    '''

    def __init__(self, train_sents):
        '''
        Constructor
        '''        
        self.tagger = ConsecutiveNPGeneChunkTagger(train_sents)
        #self.tagger = nltk.UnigramTagger(train_sents)
        
    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        print conlltags
        return nltk.chunk.util.conlltags2tree(conlltags)
