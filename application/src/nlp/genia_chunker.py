'''
Created on Aug 7, 2015

@author: varun
'''
import os
import pickle
import nltk

class GeniaChunker(nltk.ChunkParserI):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.data_loc = "/Users/varun/Downloads/biomedical/Genia4ERtraining"
        
    def read(self):
        print "Loading data from text file..... "
        sentences = []
        words = []
        iob_tags = []
        num_sentences = 0
        with open(os.path.join(self.data_loc, "Genia4ERtask1.iob2")) as iob_file:
            for i, raw in enumerate(iob_file):
                #if num_sentences > 10: break
                print "Reading line %d" % i
                raw = raw.strip()
                if raw != "":
                    line = raw.split("\t") 
                    words.append(line[0])
                    iob_tags.append(line[1])
                    
                else:
                    sentences.append((words, iob_tags))
                    words = []
                    iob_tags = []
                    num_sentences += 1
         
        print "Done"
        print "Number of sentences: %d" % (num_sentences - 1)
        
        train_data = []
        for words, iob_tags in sentences:
            tags = nltk.pos_tag(words)
            temp = []
            for i, (word, pos_tag) in enumerate(tags):
                temp.append((word, pos_tag, iob_tags[i]))
            train_data.append(temp)

        print "Dumping training data..... ",
        with open(os.path.join(self.data_loc, "train_data.pickle"), 'wb') as f:
            pickle.dump(train_data, f)
            
        print "Done!!"
        
    def train(self):
        print "Loading training data..... ",
        with open(os.path.join(self.data_loc, "train_data.pickle")) as f:
            zipped = pickle.load(f)
        print "Done!!"
        print "Zipped size: %d" % len(zipped)
        print "Size of each datum: %d" % len(zipped[0])
            
        train_data = [ [(t, c) for w,t,c in sentence] for sentence in zipped ] # t is pos tag and c is IOB chunk
        print "Training...... ",
        tagger = nltk.TrigramTagger(train_data)
        print "Done."
        print "Dumping chunker.... ",
        with open(os.path.join(self.data_loc, "trigram_chunker.pickle"), "wb") as f:
            pickle.dump(tagger, f)
        print "Done!!"
        
    def load(self):
        print "Loading trigram chunker.... ",
        with open(os.path.join(self.data_loc, "trigram_chunker.pickle")) as f:
            self.tagger = pickle.load(f)
        print "Done."
            
    def parse(self, sentence):
        sentence = nltk.word_tokenize(sentence)
        sentence = nltk.pos_tag(sentence)
        pos_tags = [pos for (word, pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                     in zip(sentence, chunktags)]
        #print conlltags
        for data in conlltags:
            print "\t".join(data)
        