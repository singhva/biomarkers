'''
Created on Dec 17, 2013

@author: varun
'''

import codecs
import re
import urllib
import urllib2
from xml.dom import minidom

import pyxb

from config import get_db_connection
from db.other.hgnc import Hgnc
import pyxb.utils.domutils as domutils
from db.ncbi.schema.ct_gov import clinical_study


class ClinicalTrials(object):
    '''
    classdocs
    '''
    base_url = "http://clinicaltrials.gov/ct2"

    def __init__(self):
        '''
        Construct a ClinicalTrials object
        '''
        #self.base_url = "http://clinicaltrials.gov/ct2"
        self.search_timeout = 60
        
    def create_search(self, term, parameters):
        query = {"term":term, "displayxml":"true"}
        if(parameters.get("lead")): query["lead"] = parameters["lead"]
        if(parameters.get("rslt")): query["rslt"] = parameters["rslt"]
        
        return query
    
    def get_search_results_count(self, term, **parameters):
        query = self.create_search(term, parameters)
        data = urllib.urlencode(query)
        #print "data is: "+data
        response = urllib2.urlopen(self.base_url+"/results?"+data).read()
        xml = minidom.parseString(response.replace("\n", ""))
        count = int(xml.getElementsByTagName("search_results")[0].attributes["count"].value)
        
        return count
    
    def get_marker_search_results(self, marker, **parameters):
        gene = Hgnc.lookup_by_symbol(marker)
        if gene:
            all_gene_ids = gene.synonyms
            all_gene_ids.append(gene.symbol)
            term = " OR ".join(all_gene_ids)
            #print "Term is: "+term
            return (term, self.get_search_results_count(term, **parameters))
        return (marker, 0)
        
    def search(self, term, **parameters):
        study_ids = []
        results_per_page = 20
        responses = []
        query = self.create_search(term, parameters)
        data = urllib.urlencode(query)
        #print "data is: "+data
        response = urllib2.urlopen(self.base_url+"/results?"+data).read()
        responses.append(response)
        xml = minidom.parseString(response.replace("\n", ""))
        count = int(xml.getElementsByTagName("search_results")[0].attributes["count"].value)
        num_pages = count/results_per_page
        if (num_pages * results_per_page) < count: num_pages = num_pages + 1
        #print num_pages
        for page in range(2, num_pages + 1):
            query["pg"] = str(page)
            data = urllib.urlencode(query)
            response = urllib2.urlopen(self.base_url+"/results?"+data).read()
            responses.append(response)
            
        for response in responses:
            xml = minidom.parseString(response.replace("\n", ""))
            clinical_studies = xml.getElementsByTagName("clinical_study")
            for study in clinical_studies:
                study_ids.append(study.getElementsByTagName("nct_id")[0].firstChild.nodeValue)
                
        #print "{} studies found, {} studies retrieved".format(str(count), str(len(study_ids)))
        #print ",".join(study_ids)
        return study_ids
    
    def find_cog_protocols(self, study_ids):
        cogid_map = {}
        cog_id_pattern = "COG"
        for count, study_id in enumerate(study_ids):
            try:
                response = urllib2.urlopen(self.base_url+"/show/"+study_id+"?displayxml=true").read()
                xml = minidom.parseString(response.replace("\n", ""))
                id_info = xml.getElementsByTagName("id_info")[0]
                secondary_ids = []                   
                drugs = []
                cog_ids = []
                interventions = xml.getElementsByTagName("intervention")
                conditions = [str(condition.firstChild.nodeValue) for condition in xml.getElementsByTagName("condition")]
                for node in id_info.childNodes:
                    if node.localName == "secondary_id":
                        #print node.firstChild.nodeValue
                        node_value = str(node.firstChild.nodeValue)
                        secondary_ids.append(node_value)
                        if re.match(cog_id_pattern, node_value): cog_ids.append(node_value)
                        
                for intervention in interventions:
                    if intervention.getElementsByTagName("intervention_type")[0].firstChild.nodeValue == "Drug":
                        drugs.append(str(intervention.getElementsByTagName("intervention_name")[0].firstChild.nodeValue))
                
                cogid_map[str(study_id)] = {"conditions":conditions, "drugs":drugs, "cog_ids":cog_ids}
                print str(count)+" - study_id: "+study_id
            except UnicodeEncodeError:
                print "error found"
            #print ",".join(interventions)
        #print cogid_map
        return cogid_map
    
    def writeToCsv(self, cogid_map):
        outfile = open("../output/cog_ids.tsv", "w")
        outfile.write("COG IDs\tDrugs\tConditions\n")
        for study_id in cogid_map:
            if(len(cogid_map[study_id].get("cog_ids")) > 0):
                cog_ids = ",".join(cogid_map[study_id].get("cog_ids"))
                drugs = ",".join(cogid_map[study_id].get("drugs"))
                conditions = ",".join(cogid_map[study_id].get("conditions"))
                outfile.write(cog_ids+"\t"+drugs+"\t"+conditions+"\n")
        outfile.close()
        
class ClinicalStudy():
    def __init__(self, study_id):
        self._id = study_id
        self._xml = None
            
    @classmethod
    def get(cls, study_id):
        db = get_db_connection()
        record = db["CLIN_TRIALS"].find_one({"STUDY_ID": study_id})
        if not record:
            try:
                response = urllib2.urlopen(ClinicalTrials.base_url+"/show/" + study_id+"?displayxml=true").read()
                study = response
                db["CLIN_TRIALS"].save({"STUDY_ID":study_id, "STUDY": response})
            except urllib2.HTTPError as e:
                print "Caught exception: "+str(e)
                return None
        
        else:
            study = record.get("STUDY")
            
        doc = domutils.StringToDOM(study)
        pyxb.RequireValidWhenParsing(False)
        cs = ClinicalStudy(study_id)
        cs._xml = clinical_study.createFromDOM(doc.documentElement)
        return cs        
            
    def get_title(self):
        return self._xml.official_title
    
    def get_phase(self):
        return self._xml.phase
    
    def get_enrolled_patients_count(self):
        return self._xml.enrollment.content()
    
    def get_patient_demographics(self):
        eligibility = self._xml.eligibility
        demographics = {}
        demographics["gender"] = eligibility.gender.lower()
        demographics["minimum_age"] = 0
        demographics["maximum_age"] = 100
        demographics["count"] = self.get_enrolled_patients_count()
        
        if re.match("\d+", eligibility.minimum_age):
            demographics["minimum_age"] = int(re.match("\d+", eligibility.minimum_age).group(0))
        if re.match("\d+", eligibility.maximum_age):
            demographics["maximum_age"] =int(re.match("\d+", eligibility.maximum_age).group(0))
            
        demographics["inclusion_criteria"] = codecs.encode(eligibility.criteria.textblock, "utf-8")
        return demographics
    
    def get_drugs(self):
        drugs = set()
        for intervention in self._xml.intervention:
            if intervention.intervention_type == "Drug" or intervention.intervention_type=="Biological":
                drugs.add(intervention.intervention_name)
        return list(drugs)
        