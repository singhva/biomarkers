'''
Created on Jul 15, 2015

@author: varun
'''
import re
import nltk
from types import StringTypes
from types import IntType
from pattern.text.en import parsetree
from pattern.text.search import search
from pattern.text.en import number
from db.ncbi.pubmed import Pubmed
from data.process_pdf import PdfReader

class Evidence(object):
    '''
    classdocs
    '''
    month = "(january|february|march|april|may|june|july|august|september|october|november|december)"
    meta_analysis_re = re.compile("meta[-]?analysis", re.IGNORECASE)
    review_re = re.compile(r"review|systematic|comprehensive")
    study_re = re.compile("[sS]tudies|[tT]rials|RCT[s]?|prospective randomized trials|randomized trials|articles|papers|clinical studies")
    include_re = re.compile("[iI]ncluded|[iI]dentified|analyzed|enrolled|performed|published")
    #patients_re = re.compile("[pP]atients|[mM]en|[wW]omen")
    randomized_re = re.compile(r"[rR]andomized|[rR]andomised|randomly")
    case_control_re = re.compile("case[-]?control", re.IGNORECASE)
    case_or_control_re = re.compile("case|control", re.IGNORECASE)
    extracted_re = re.compile(r"extracted|cut|isolated|dissected|collected")
    count_patient_grammar = r"""
        CHUNK: {<CD><.*>*<NNS>}
    """
    expression_re = re.compile("[-\s]?(?P<expr>overexpress|underexpress)(?P<suffix>:ing|ion|ied|ication)?", re.IGNORECASE)

    def __init__(self, pubmed):
        '''
        Constructor
        '''
        self.base_dir = "/Users/varun/Documents/papers/NLP/"
        if isinstance(pubmed, StringTypes) or isinstance(pubmed, IntType):
            self.pubmed = Pubmed.get_publication_from_pubmed(unicode(pubmed))
            
        else: self.pubmed = pubmed
        self.pdf = None
        self.level = None
        self.patient_count = 0
    
    def find_level(self):            
        if self.is_meta_analysis():
            print "Meta analysis"
            
        elif self.is_review():
            print "Review"
            
        elif self.is_randomized():
            print "Randomized Control Trial"
            if self.is_biomarker_driven():
                print "Biomarker driven"
                if self.is_arm_biomarker_driven():
                    print "Study arm biomarker driven"
                else:
                    print "Study arm not biomarker driven"
                    
        elif self.is_observational():
            print "Observational study"
            if self.is_case_control():
                print "Case control study"
                    
            elif self.is_cohort_study():
                print "Cohort study"
                
            if self.is_low_powered():
                print "Low powered"
            else:
                print "High powered"
                
            if self.is_biomarker_driven():
                print "Biomarker driven"
                    
        else:
            print "Can't determine"
            
            
    def is_meta_analysis(self):
        return "Meta-Analysis" in self.pubmed.get_publication_types() or self.meta_analysis_re.search(self.pubmed.get_title())
    
    def is_review(self):
        return "Review" in self.pubmed.get_publication_types() or ("Systematic Reviews" in self.pubmed.get_publication_types()) or (self.review_re.search(self.pubmed.get_title()) is not None)
    
    def is_treatment(self):
        pass
    
    def is_observational(self):
        return "Observational Study" in self.pubmed.get_publication_types() or self.is_cohort_study() or self.is_case_control() or (self.get_patient_count() > 0)
    
    def is_randomized(self):
        phase3_trials = ["Randomized Controlled Trial", "Clinical Trial, Phase III"]
        pub_types_found = [trial_type for trial_type in self.pubmed.get_publication_types() if trial_type in phase3_trials]
        mesh_types_found = [trial_type for trial_type in self.pubmed.get_mesh_terms() if trial_type in phase3_trials]
        return  (len(pub_types_found) > 0) or ((len(mesh_types_found) > 0)) or self.randomized_re.search(self.pubmed.get_title())
    
    def is_low_powered(self):
        '''
        print "inside low powered"
        count = 0
        if self.case_or_control_re.search(self.pubmed.get_abstract()):
            cp = nltk.RegexpParser(self.count_patient_grammar)
            sentences = nltk.sent_tokenize(self.pubmed.get_abstract())
            for sentence in sentences:
                if self.case_or_control_re.search(sentence) and self.patients_re.search(sentence):
                    tree = cp.parse(nltk.pos_tag(nltk.word_tokenize(sentence)))
                    for subtree in tree.subtrees():
                        if subtree.label() == "CHUNK": 
                            print " ".join(nltk.tag.untag(subtree))
                            count = int(list(subtree)[0][0])
        '''
        return self.get_patient_count() < 50
    
    def is_cohort_study(self): # PUT GENERIC LOGIC FOR A GROUP OF PATIENTS
        cohort_study_types = ["Cohort Studies", "Longitudinal Studies", "Follow-Up Studies"]
        mesh_terms_found = [mesh_term for mesh_term in self.pubmed.get_mesh_terms() if mesh_term in cohort_study_types]
        return (len(mesh_terms_found) > 0) or self.is_prospective_cohort() or self.is_retrospective_cohort()
            
    def is_case_control(self):
        return ("Case-Control Studies" in self.pubmed.get_mesh_terms()) or self.case_control_re.search(self.pubmed.get_title()) or self.case_control_re.search(self.pubmed.get_abstract())
    
    def is_retrospective_cohort(self):
        return ("Retrospective Studies" in self.pubmed.get_mesh_terms()) or ("retrospective" in self.pubmed.get_title().lower())
    
    def is_prospective_cohort(self):
        return ("Prospective Studies" in self.pubmed.get_mesh_terms()) or ("prospective" in self.pubmed.get_title().lower())
    
    def get_patient_count(self):
        #patients_grammar = "CHUNK:{<CD><JJ.*>*<VB.*>*<NN.*>}"
        #cp = nltk.RegexpParser(patients_grammar)
        if self.patient_count > 0: 
            print "Patient count: %d" % self.patient_count
            return self.patient_count
        
        patients_re = re.compile(r"patients|men|women|cases")
        new_patient_grammar = "CD (VBD|NNP|JJ)+ {}".format(patients_re.pattern)
        text = self.pubmed.get_title() + "\n" + self.pubmed.get_abstract()
        found_match = []
        
        if patients_re.search(text):
            sents = nltk.sent_tokenize(text)
            for sent in sents:
                s = parsetree(sent)
                search_result = search(new_patient_grammar, s)
                if search_result is not None and len(search_result) > 0:
                    found_match.append(search_result[0].constituents()[0].string)
                    self.patient_count = sorted([[number(word.string) for word in result.words if word.tag=='CD'][0] for result in search_result])[-1]
                    print "Patient count: %d" % self.patient_count
                    return self.patient_count
                '''
                subtrees = cp.parse(nltk.pos_tag(nltk.word_tokenize(sent))).subtrees()
                chunked_trees = [ sub for sub in list(subtrees) if sub.label() == "CHUNK" and patients_re.search(nltk.tag.untag(sub)[-1])]
                if len(chunked_trees) > 0:
                    patients_match_found = True
                    found_match.append(" ".join(nltk.tag.untag(chunked_trees[0])))
                    break
                '''
            
        if self.pubmed.download_pdf():
            pdf = self.pubmed.get_pdf()
            mm = pdf.sections[PdfReader.MM]["text"]
            sents = nltk.sent_tokenize("\n".join(mm[:10]))
            for sent in sents:
                s = parsetree(sent)
                search_result = search(new_patient_grammar, s)
                if search_result is not None and len(search_result) > 0:
                    found_match.append(search_result[0].constituents()[0].string)
                    self.patient_count = sorted( [[number(word.string) for word in result.words if word.tag=='CD'][0] for result in search_result]  )[-1]
                    print "Patient count: %d" % self.patient_count
                    return self.patient_count
                '''
                subtrees = cp.parse(nltk.pos_tag(nltk.word_tokenize(sent))).subtrees()
                chunked_trees = [ sub for sub in list(subtrees) if sub.label() == "CHUNK" and patients_re.search(nltk.tag.untag(sub)[-1]) ]
                if len(chunked_trees) > 0 :
                    patients_match_found = True
                    found_match.append(" ".join(nltk.tag.untag(chunked_trees[0])))
                    break
                '''
    
    def is_biomarker_driven(self):
        expression_verb_re = re.compile(r"expressed|under[-]?expressed|over[-]?expressed", re.IGNORECASE)
        expression_noun_re = re.compile(r"expression[s]?|under[-]?expression|over[-]?expression|negative|positive|polymorphism[s]?|SNP[s]?|mutation[s]?|status|role|level[s]?", re.IGNORECASE)
        precision_re = re.compile(r"personalize[d]?|customize[d]?|tailored|individual|individualized")
        
        associate_noun_re = re.compile(r"correlation[s]?|link|cause|effect|significance|importance|indication|association|relationship|modulation", re.IGNORECASE)
        associate_verb_past_participle_re = re.compile("associated|linked|affected")
        
        effect_verb_re = re.compile(r"predict[s]?\b|modulate[s]?\b|impact\b|correlate\b", re.IGNORECASE)
        predict_noun_re = re.compile(r"prediction|predicting", re.IGNORECASE)
        predict_adj_re = re.compile(r"prognostic|predictive|correlative|indicative|associative", re.IGNORECASE)
        
        important_adj_re = re.compile(r"important|significant")
        outcome_re = re.compile(r"efficacy|response|outcome[s]?|survival|prognosis", re.IGNORECASE)
        markers_re = re.compile(r"marker[s]?|biomarker[s]?", re.IGNORECASE)


        title = self.pubmed.get_title()
        abstract = self.pubmed.get_abstract()
        text = title + "\n" + abstract
        found_match = []
        
        if expression_noun_re.search(title):
            found_match.append(expression_noun_re.search(title))
            if effect_verb_re.search(title):
                found_match.append(effect_verb_re.search(title))
                
            elif associate_verb_past_participle_re.search(title):
                found_match.append(associate_verb_past_participle_re.search(title)) 
                
            elif associate_noun_re.search(title):
                found_match.append(associate_noun_re.search(title))
                
            elif predict_adj_re.search(title):
                found_match.append(predict_adj_re.search(title))
                
            elif predict_noun_re.search(title):
                found_match.append(predict_noun_re.search(title))
                
        elif precision_re.search(title):
            found_match.append(precision_re.search(title))
            
        elif predict_adj_re.search(title):
            found_match.append(predict_adj_re.search(title))
            if markers_re.search(title):
                found_match.append(markers_re.search(title))
                
        elif predict_noun_re.search(title):
            found_match.append(predict_noun_re.search(title))
                
        elif effect_verb_re.search(title):
            found_match.append(effect_verb_re.search(title))                      
        
        if len(found_match) > 1 and outcome_re.search(text):
            found_match.append(outcome_re.search(text))

        if len(found_match) > 2:           
            print "*** EVIDENCE ****"
            print "Keywords: ",
            for match in found_match:
                if isinstance(match, StringTypes): print match + ", ",
                else: print match.group(0) + ", ",
            print "\n"
            return True
                
        else:
            return False
        
    def is_arm_biomarker_driven(self):
        arm_re = re.compile(r"\b[a-zA-Z]*\b and \b[a-zA-Z]*\b arms|\b[\(\)a-zA-Z]*\b arm|\b[a-zA-Z]*\b group")
        text = self.pubmed.get_title() + "\n" + self.pubmed.get_abstract()
        match = arm_re.search(text)
        if match:
            annotations = self.pubmed.retrieve_pubtator_annotations()
            gene_annotations = annotations["genes"]
            chemical_annotations = annotations["chemicals"]
            genes_re = re.compile(r"|".join(gene_annotations))
            chemicals_re = re.compile(r"|".join(chemical_annotations))
            sentences = nltk.sent_tokenize(text)
            for sent in sentences:
                if arm_re.search(sent) and genes_re.search(sent) and chemicals_re.search(sent):               
                    print "Biomarker driven: arm(%s), genes(%s), chemicals(%s)" % (arm_re.search(sent).group(0), genes_re.search(sent).group(0), chemicals_re.search(sent).group(0))
                    return True
                    
                elif arm_re.search(sent) and chemicals_re.search(sent):
                    print "Biomarker driven: arm(%s), chemicals(%s)" % (arm_re.search(sent).group(0), chemicals_re.search(sent).group(0))
                    return False
                
                else: return False
    
    def is_retrospective_analysis_of_rct(self):
        pass