'''
Created on Apr 8, 2014

@author: varun
'''
import os
import sys
import glob
import copy
from datetime import datetime
import re
import urllib2
import abc
import cherrypy
import codecs
import requests
from urlparse import urlparse
from bs4 import BeautifulSoup 

from Bio import Medline
import becas
import nltk

from clinicaltrials import ClinicalStudy
from data.database import DBObject
from entrez import ICBIEntrez
from db.other.hgnc import Hgnc
from db.other.medic import Medic
from data.process_pdf import PdfReader
from nlp.annotations import ManualAnnotations, NlpAnnotations, GeneAnnotation, DiseaseAnnotation, Annotation


class Pubmed(ICBIEntrez, DBObject):
    '''
    classdocs
    '''
    EMAIL = "vs454@georgetown.edu"
    ENTREZ_DB = "pubmed"
    COLLECTION = "PUBLICATIONS"
    FK = "RAW.PMID"
    RETMAX = 1000
    STALE_ANNOTATION_STATUS = "STALE"
    
    
    MARKER_STATUS = ["positive", "negative", "unknown"]
    VARIANT_SOURCE = ["somatic", "germline", "unknown"]
    PUBLICATION_TYPES = ['Addresses', 'Autobiography', 'Bibliography', 'Biography', 'Case Reports', 'Classical Article', 'Clinical Conference', 'Clinical Trial', 
                         'Clinical Trial, Phase I', 'Clinical Trial, Phase II', 'Clinical Trial, Phase III', 'Clinical Trial, Phase IV', 'Comment', 
                         'Comparative Study', 'Congresses', 'Consensus Development Conference', 'Consensus Development Conference, NIH', 'Controlled Clinical Trial', 
                         'Corrected and Republished Article', 'Dataset', 'Dictionary', 'Directory', 'Duplicate Publication', 'Editorial', 'Electronic Supplementary Materials', 
                         'English Abstract', 'Evaluation Studies', 'Festschrift', 'Government Publications', 'Guideline', 'Historical Article', 'In Vitro', 
                         'Interactive Tutorial', 'Interview', 'Introductory Journal Article', 'Journal Article', 'Lectures', 'Legal Cases', 'Legislation', 'Letter', 
                         'Meta-Analysis', 'Multicenter Study', 'News', 'Newspaper Article', 'Observational Study', 'Overall', 'Patient Education Handout', 
                         'Periodical Index', 'Personal Narratives', 'Portraits', 'Practice Guideline', 'Pragmatic Clinical Trial', 'Published Erratum', 
                         'Randomized Controlled Trial', 'Research Support, American Recovery and Reinvestment Act', 'Research Support, N.I.H., Extramural', 
                         'Research Support, N.I.H., Intramural', "Research Support, Non-U.S. Gov't", "Research Support, U.S. Gov't, Non-P.H.S.", 
                         "Research Support, U.S. Gov't, P.H.S.", 'Research Support, U.S. Government', 'Retracted Publication', 'Retraction of Publication', 'Review', 
                         'Scientific Integrity Review', 'Systematic Reviews', 'Technical Report', 'Twin Study', 'Validation Studies', 'Video-Audio Media', 'Webcasts']

    SORT_KEY_PUB_DATE = ("pub date", "Publ. Date")
    SORT_KEY_RECENTLY_ADDED = ("recently added", "Recently Added")
    SORT_KEY_JOURNAL = ("journal", "Journal Title")
    SORT_KEY_RELEVANCE = ("relevance", "Relevance")
    SORT_KEYS = [SORT_KEY_RECENTLY_ADDED, SORT_KEY_PUB_DATE, SORT_KEY_JOURNAL, SORT_KEY_RELEVANCE]
    
    FILTER_KEY_JOURNAL = "journal"   
    FILTER_KEYS = [FILTER_KEY_JOURNAL]
    
    CANCER_REGEX = "[cC]ancer|CANCER|[cC]arcinoma|[lL]ymphoma"
    DOI_REGEX = re.compile('(AID\s-\s)?(?P<DOI>10[.][0-9]{4,}[^\s"/<>]*/[^\s"<>]+)(\s\[doi\])?', re.IGNORECASE)
    #TREATMENT_ARMS = re.compile()
    
    def __init__(self, pmid, db_record = None):
        '''
        Constructor
        '''
        DBObject.__init__(self, db_record)
        ICBIEntrez.__init__(self, pmid)
        self._raw = None
        self._annotations = None
        self._clinical_trials = None
        self._features = None
        self._data = {}
        self.full_text = None
        self._has_fulltext = False
        self._cached_pdf = None
        
    @classmethod
    def medline_to_class(cls, medline_record):
        if medline_record:
            pubmed = cls(pmid = medline_record.get("PMID"))
            pubmed._raw = medline_record
            pubmed._fetch_annotations()
            return pubmed
    
    @classmethod
    def db_to_class(cls, db_record):
        pmid = db_record.get("RAW").get("PMID")
        pubmed = Pubmed(pmid, db_record = db_record)
        pubmed._raw = db_record.get("RAW")
        pubmed._annotations = db_record.get("ANNOTATIONS")            
        pubmed._clinical_trials = db_record.get("CLINICAL_TRIALS")
        pubmed._data = db_record.get("DATA") or {}
        pubmed._has_fulltext = db_record.get("HAS_FULL_TEXT") or False
        
        if(pubmed.is_annotation_stale()):
            pubmed._fetch_annotations()
            pubmed.save()
        return pubmed
    
    def class_to_db(self):
        bson = {}
        if self._id:
            bson["_id"] = self._id
        bson["RAW"] = self.get_raw()
        bson["PMID"] = self.get_pmid()
        if self._annotations:
            bson["ANNOTATIONS"] = self._annotations
        if self._clinical_trials: 
            bson["CLINICAL_TRIALS"] = self.get_clinical_trial_ids()
        if self._data:
            bson["DATA"] = self._data

        return bson
    
    @classmethod
    def get_publications_from_pmids(cls, idlist, refresh=False):
        orig_id_list = copy.copy(idlist)
        publications = []
        if refresh:
            publications.extend(orig_id_list)
        else:
            pubmeds_from_db = cls.get_all_by_fks(orig_id_list)
            for pubmed in pubmeds_from_db:
                orig_id_list.remove(pubmed.get_pmid())
                
            publications.extend(pubmeds_from_db)
        print "%d pmids to be retrieved from Pubmed" % len(orig_id_list)
            
        if len(orig_id_list) > 0:
            handle = cls.fetch(orig_id_list, rettype="medline", retmode="text")           
            if handle: 
                fetched_records = list(Medline.parse(handle))
                for record in fetched_records:
                    pubmed = Pubmed.medline_to_class(record)
                    if pubmed:
                        try:
                            print "About to save - %s" % pubmed.get_pmid()
                            pubmed.save()
                            publications.append(pubmed)
                        except:
                            pass
        
        #publications.sort(key=lambda pub: idlist.index(pub.get_pmid())) #publications may not contain all ids from orig_id_list
        return publications
        
    @classmethod
    def get_publication_from_pmid(cls, pubmed_id, refresh=False):
        pubmeds = cls.get_publications_from_pmids([pubmed_id], refresh)
        return pubmeds[0] if len(pubmeds) > 0 else None
    
    @classmethod
    def get_publication_from_pubmed(cls, pubmed_id):
        handle = cls.fetch(pubmed_id, rettype="medline", retmode="text")
        if handle:
            fetched_records = list(Medline.parse(handle)) 
            return Pubmed.medline_to_class(fetched_records[0])
        
    def populate_features(self):
        features = {}
        trial_info = self.get_clinical_trial_info()
        time_delta = datetime.today() - self.get_publication_date()
        features["is_clinical_trial"] = len(trial_info) > 0
        features["is_clinical_trial_phase1"] = "Clinical Trial, Phase I" in trial_info
        features["is_clinical_trial_phase2"] = "Clinical Trial, Phase II" in trial_info
        features["is_clinical_trial_phase3"] = "Clinical Trial, Phase III" in trial_info
        features["is_clinical_trial_phase4"] = "Clinical Trial, Phase IV" in trial_info
        features["is_randomized"] = "Randomized Controlled Trial" in trial_info
        features["is_newer_than_10_years"] = time_delta.days < 3650
        self._features = features
        
    def get_manual_annotations(self):
        return ManualAnnotations.get_by_pmid(self.get_pmid())
    
    def get_nlp_annotations(self):
        raw_annotations = self._record.get("ANNOTATIONS")
        nlp_annotations = NlpAnnotations(self.get_pmid())
        if "GENE" in raw_annotations:
            raw_annotation = raw_annotations["GENE"]
            hgnc_genes = Hgnc.lookup_by_entrez_id(raw_annotation.keys())
            for hgnc_gene in hgnc_genes:
                mentions = raw_annotation.get(hgnc_gene.entrez_id).get("MENTIONS")
                annotation = GeneAnnotation(hgnc_gene.entrez_id, Annotation.SYSTEM)
                annotation.normalized_text = hgnc_gene.symbol
                for mention in mentions:
                    annotation.add_mention(mention, 0, 0)
                nlp_annotations._gene_annotations.append(annotation)
                
        if "DISEASE" in raw_annotations:
            raw_annotation = raw_annotations["DISEASE"]
            medic_diseases = Medic.get_all_by_fks([key[5:] for key in raw_annotation.keys()])
            for medic_disease in medic_diseases:
                mentions = raw_annotation.get(medic_disease.get_disease_id()).get("MENTIONS")
                annotation = DiseaseAnnotation(medic_disease.get_disease_id(), Annotation.SYSTEM)
                annotation.normalized_text = medic_disease.get_disease_name()
                for mention in mentions:
                    annotation.add_mention(mention, 0, 0)
                nlp_annotations._disease_annotations.append(annotation)
                
        return nlp_annotations
    
    def _fetch_annotations(self):
        """
        This method fetched NLP annotations which have been uploaded to the ANNOTATIONS table from another process/script.
        This allows the NLP annotations of a PUBMED ID to be updated based on updated data from another source
        """
        try:
            #becas.email = Pubmed.EMAIL
            #becas.timeout = Pubmed.TIMEOUT
            #annotations = becas.annotate_text((pubmed.get_title() or "") +"\n" + (pubmed.get_abstract() or ""))
            #print "Fetching annotation"
            record = self.join_with_another_collection("ANNOTATIONS", "PMID")
            if record:
                del record["_id"]
                del record["PMID"]
                annotations = record
                annotations["STATUS"] = ""
                self._annotations = annotations
        except IOError as e:
            print e
            return None
        
    def is_annotation_stale(self):
        return (self._annotations is None) or self._annotations["STATUS"] == Pubmed.STALE_ANNOTATION_STATUS
        
    def get_pmid(self):
        return self.entrez_id
    
    def get_raw(self):
        return self._raw
    
    def get_abstract(self):
        return self.get_raw().get("AB", "")
    
    def get_title(self):
        return self.get_raw().get("TI", "")
    
    def get_journal(self):
        return self.get_raw().get("TA")
    
    def get_clinical_trial_info(self):
        types = self.get_raw().get("PT")            
        return [ p_type for p_type in types if "Trial" in p_type ]    
    
    def is_clinical_trial(self):
        return len(self.get_clinical_trial_info()) > 0   
    
    def get_clinical_trial_ids(self):
        trial_ids = []
        for trial in self.get_clinical_trials():
            trial_ids.append(trial._id)
        return trial_ids
    
    def _fetch_clinical_trials(self): # THIS SHOULD BE CHANGED TO REFLECT CLINICAL TRIAL IDS FIELD IN _record
        '''
        if self.clinical_trial_ids is None:
            ct = ClinicalTrials()
            term = self._id+" [PUBMED-IDS]"
            self.clinical_trial_ids = ct.search(term)
        '''
        clinical_trials = []
        secondary_ids = self.get_raw().get("SI", [])
        for secondary_id in secondary_ids:
            if secondary_id.startswith("ClinicalTrials.gov"):
                trial_id = secondary_id.split("/")[1]
                print "Trial id is: "+trial_id
                cs = ClinicalStudy.get(trial_id)
                clinical_trials.append(cs)
                
        self._clinical_trials = clinical_trials
        
    def get_clinical_trials(self):        
        if not self._clinical_trials: 
            self._fetch_clinical_trials()
            
        return self._clinical_trials
    
    def get_publication_types(self):
        return self.get_raw().get("PT")
    
    def get_mesh_terms(self):
        return self.get_raw().get("MH")
    
    def get_publication_date(self):
        return datetime.strptime(self.get_raw().get("EDAT"), "%Y/%m/%d %H:%M")
    
    def get_doi(self):
        AID = self.get_raw().get("AID")
        if AID is not None:
            for aid in AID:
                match = Pubmed.DOI_REGEX.match(aid)
                if match: return match.group("DOI")
                
    def get_gene_mentions(self):
        print "Inside Pubmed get_gene_mentions"
        url = "http://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/PubTator/abstract_ann.cgi?Disease=9&Gene=1&Chemical=0&Mutation=0&Species=0&pmid={}".format(self.entrez_id)
        response = urllib2.urlopen(url).read()
        response = response[179:-22].strip()
        genes = set()
        for i, line in enumerate(response.split("\n")):
            if i > 1:
                line = line.split("\t")
                genes.add(line[3].strip())
                
        return list(genes)
    
    def get_patient_characteristics(self):
        '''
        text = self.get_abstract()
        sentences = nltk.sent_tokenize(text)
        matched = []
        subject_words_pattern = "[wW]?[o]?m[ae]n"
        verbs_pattern = "(?:assign|recruit)(?:ed)"
        for sentence in sentences:
            #words = [word.lower() for word in nltk.word_tokenize(sentence)]
            if re.search(subject_words_pattern, sentence) and re.search(verbs_pattern, sentence):
                matched.append(sentence)
                
        return matched
        '''
        trials = self._clinical_trials
        if(len(trials) > 0):
            return trials[0].get_patient_demographics()
    
        else:
            count_regex = "(?P<number>[\d]+)[\s]*(?:men|women|patients)"
            count = 0
            if re.search(count_regex, self.get_abstract()):
                count = re.search(count_regex, self.get_abstract()).group("number")          
            return {"gender":"both", "minimum_age":0, "maximum_age":100, "inclusion_criteria":"", "count":count}
        
        '''
        if len(trials.keys()) > 0:
            for trial_id in trials:
                ct = trials[trial_id]
                return ct.get_patient_demographics()
        '''
    
    def get_disease_annotations(self):
        return self._annotations.get("DISEASE")
        
    def get_gene_annotations(self):
        return self._annotations.get("GENE")        
    
    def get_cancer_types(self, annotations):
        cancers = {}
        for entity in annotations["entities"]:
            annotate_1 = entity.split(":")
            if annotate_1[-1].startswith("DISO"):
                entity = entity.split("|")
                disease_name = entity[0]
                umls = entity[1].split(":")[1]
                if re.search(Pubmed.CANCER_REGEX, disease_name):
                    key = (entity[1].split(";"))[0]
                    cancer_name = annotations["ids"][key]
                    cancers[umls] = cancer_name["name"]

        print str(cancers)
        return cancers

    '''
    def get_drugs(self, annotations):
        drug_names = set()
        drugs = {}
        db = get_db_connection()
        trials = self.get_clinical_trials()
        for trial in trials:
            drug_names.update(trial.get_drugs())
            
        for drug_name in drug_names:
            drug_from_drugbank = db["DRUGS"].find_one({"NAME":{"$regex":drug_name, "$options": 'i'}})
            if drug_from_drugbank is not None: drugs[drug_from_drugbank["DB_ID"]] = drug_from_drugbank["NAME"]
            
        return drugs
    '''
    
    def get_genes(self, annotations):
        genes = {}
        for entity in annotations["entities"]:
            annotate_1 = entity.split(":")
            if annotate_1[-1].startswith("PRGE"):
                gene_name = entity.split("|")[0]
                hgnc = Hgnc.lookup_by_uniprot_id(annotate_1[1])
                if hgnc is not None:
                    genes[gene_name] = hgnc.symbol      
        print "Genes are: "+str(genes)
        return genes
    
    def get_marker_details(self, annotations):
        abstract = self.get_abstract()
        sentences = nltk.sent_tokenize(abstract)
        gene_names = self.get_genes(annotations)
        statuses = {}
        for name in gene_names:
            #print "Marker is: {}".format(marker)
            evidences = []
            regex = name
            regex += "[-\s]?(?P<expr>\+|\-|negative|positive)"
            #regex += "[-\s]?(?P<expr>\+|\-|negative|positive|overexpress|underexpress|amplif|coamplif|aberrat|delet)(?P<suffix>:ing|ion|ied|ication)?"
            #print "Regex is: "+regex
            status = "unknown"
            for sentence in sentences:
                if re.search(regex, sentence):
                    match = re.search(regex, sentence)
                    status = match.group("expr")
                    if status == "+": status = "positive"
                    if status == "-": status = "negative"
                    #if match.group("suffix"): status += match.group("suffix")
                    evidences.append(sentence)
                
            statuses[gene_names[name]] = {"status":status}
            if(len(evidences) > 0): statuses[gene_names[name]]["evidence"] = evidences[0]
            else: statuses[gene_names[name]]["evidence"] = "unknown"
            
        return statuses
    
    def get_variant_source(self, annotations):
        abstract = self.get_abstract()
        sentences = nltk.sent_tokenize(abstract)
        gene_names = self.get_genes()
        sources = {}
        for name in gene_names:
            evidences = []
            regex = name
            regex += "[-\s]?(?P<source>[sS]omatic|[gG]erm[-]?line)"
            source = "unknown"
            for sentence in sentences:
                match = re.search(regex, sentence)
                if match:
                    source = match.group("source").lower()
                    evidences.append(sentence)
                    
            if(len(evidences) == 0): evidences = ["unknown"]
            sources[gene_names[name]] = {"source":source, "evidence":evidences[0]}
            
        return sources
          
    def get_gene_expression(self, annotations):
        '''
        Regex example: (HER2)?[-\s]?(?P<expr>overexpress|underexpress)(?P<suffix>:ing|ion|ied|ication)?(.+?)(of)[\s](HER2)?
        ''' 
        abstract = self.get_abstract()
        sentences = nltk.sent_tokenize(abstract)
        gene_names = self.get_genes()
        expressions = {}
        for name in gene_names:
            evidences = []
            regex = "({})?".format(name)
            regex += "[-\s]?(?P<expr>overexpress|underexpress)(?P<suffix>:ing|ion|ied|ication)?"
            regex += "(.+?)(of)[\s]"
            regex += "({})?".format(name)
            expression = "unknown"
            for sentence in sentences:
                match = re.search(regex, sentence)
                if match:
                    expression = match.group("expr").lower()
                    evidences.append(sentence)
                    
            if(len(evidences) == 0): evidences = ["unknown"]
            expressions[gene_names[name]] = {"expression":expression, "evidence":evidences}
            
        return expressions
    
    def get_treatment_arms(self):
        pass               
    
    def get_results_of_study(self):
        result = self._data.get("RESULTS")
        results_regex = "(?:Result[s]?|RESULT[S]?|Finding[s]?|FINDING[S]?)"
        conclusions_regex = "(?:INTERPRETATION[S]?|CONCLUSION[S]?)"
        
        if not result:
            pass
        
        else:
            abstract = self.get_abstract()
            print "no full text"
            if re.search(results_regex, abstract):
                start = re.search(results_regex, abstract).start()
                if re.search(conclusions_regex, abstract):
                    end = re.search(conclusions_regex, abstract).start()
                    result = abstract[start:end]
                result = abstract[start:]
                
        return result
        
    def get_conclusion(self):
        conclusions_regex = "(?:Interpretation[s]?|INTERPRETATION[S]?)"
        abstract = self.get_abstract()
        if re.search(conclusions_regex, abstract):
            start = re.search(conclusions_regex, abstract).start()
            return abstract[start:]
        
    def retrieve_pubtator_annotations(self):
        pubtator_url = "http://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/BioConcept/{}/PubTator/"
        r = requests.get(pubtator_url.format(self.get_pmid()))
        genes = []
        diseases = []
        chemicals = []
        text = r.text
        if text is not None and text.strip() != "":
            for i, raw in enumerate(text.split("\n")):
                if i > 1 and raw.strip() != "":
                    line = raw.split("\t")                    
                    if line[-2] == "Gene": genes.append(line[-3])
                    elif line[-2] == "Disease": diseases.append(line[-3])
                    elif line[-2] == "Chemical": chemicals.append(line[-3])
                
        return { "genes" : genes, "diseases" : diseases, "chemicals" : chemicals }
        
    def download_pdf(self, base_dir = os.path.join(os.environ["HOME"], "Documents", "papers", "NLP")):
        if os.path.exists(os.path.join(base_dir, self.get_journal())):
            for file1 in os.listdir(os.path.join(base_dir, self.get_journal())):
                if file1.startswith(self.get_pmid()):
                    print "File exists: " + file1
                    return True

        pdf_re = re.compile("(download|get|full text)?[\W]*pdf", re.IGNORECASE)
        doi = self.get_doi()
        if doi is None:
            return False
        
        url = "http://dx.doi.org/"
        headers={'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'}
        r = requests.get(url + doi, allow_redirects=True)
        print "URL is: " + r.url
        new_url = urlparse(r.url)
        #print "new url: " + new_url.hostname
        content_type = r.headers['content-type']
        #print "Content type: " + content_type
        pdf_links = {}
        if (content_type is not None) and content_type.lower().startswith("text/html"):
            html_doc = r.text
            soup = BeautifulSoup(html_doc, 'html.parser')
            for tag in soup.find_all('a'):
                for content in tag.contents:
                    try:
                        if content is not None and pdf_re.search(codecs.decode(content)):
                            print "Download link: " + tag.get("href")
                            href = tag.get("href")
                            if href in pdf_links:
                                pdf_links[href] += 1
                            else:
                                link = urlparse(href)
                                score = (href.endswith(".pdf") | href.endswith(".PDF")) + ("/pdf/" in href) + (link.scheme == '')
                                pdf_links[href] = score
                        #else: return False
                    except:
                        #print "Unexpected error:", sys.exc_info()[0]
                        pass
                    
        #print pdf_links
        if len(pdf_links.keys()) > 0:
            pdf_links = sorted(pdf_links.items(), key = lambda x: -x[1])
            #print pdf_links
            directory = os.path.join(base_dir, self.get_journal())
            if not os.path.exists(directory):
                try:
                    os.makedirs(directory)
                except:
                    print "Unable to make directory " + directory
                    return False
                
            pdf_link = pdf_links[0][0] # Get the first link from the sorted list
            pdf_link = pdf_link[1:] if pdf_link[0] == '/' else pdf_link
            pdf_link = pdf_link.strip()
            pdf_link = new_url.scheme + "://" + new_url.hostname + "/" + pdf_link if (urlparse(pdf_link).scheme=='') else pdf_link
            
            pdf_response = requests.get(pdf_link.strip())
            content_type = pdf_response.headers['content-type']
            if (content_type is not None) and (not content_type.lower().startswith("application/pdf")):
                if pdf_link.lower().endswith("pdf+html"): # Can check for other kinds of file extensions
                    pdf_link = pdf_link.split("+html")[0]
                elif pdf_link.lower().endswith("epdf"):
                    pdf_link = re.sub("epdf", "pdf", pdf_link)
                pdf_link = pdf_link.strip()
                    
                print "PDF link: " + pdf_link
                    
                pdf_response = requests.get(pdf_link, headers=headers)
                content_type = pdf_response.headers['content-type']
                    
            if (content_type is not None) and (content_type.lower().startswith("application/pdf")):   
                print "Downloading pdf..... ",
                filename = ""
                if "Content-Disposition" in pdf_response.headers:
                    filename = pdf_response.headers["Content-Disposition"].split("=")
                    filename = filename[1].strip('"') if len(filename) > 0 else ""
                if filename.strip() == "" or not filename.lower().endswith("pdf"):
                    filename = self.get_pmid() + ".pdf"
                else: 
                    filename = self.get_pmid() + "_" + filename
                print filename + "... done"
                with open(directory + "/" + filename, 'wb') as fd:
                    for chunk in pdf_response.iter_content(1024):
                        fd.write(chunk)
                        
                return True
            
        return False    
        
    
    def get_pdf(self, base_dir = os.path.join(os.environ["HOME"], "Documents", "papers", "NLP")):
        if self._cached_pdf is not None: return self._cached_pdf
        elif os.path.exists(os.path.join(base_dir, self.get_journal())):
            for file1 in os.listdir(os.path.join(base_dir, self.get_journal())):
                if file1.startswith(self.get_pmid()):
                    pdf = PdfReader(os.path.join(base_dir, self.get_journal(), file1))
                    pdf.parse()
                    self._cached_pdf = pdf
                    #print "File exists: " + file1
                    #return os.path.join(base_dir, self.get_journal(), file1)
                    return pdf