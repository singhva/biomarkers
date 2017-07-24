'''
Created on May 21, 2014

@author: varun
'''
import difflib
import json

import cherrypy

from db.other.drug import Drug
from db.other.hgnc import Hgnc
from db.other.medic import Medic
from db.ncbi.clinicaltrials import ClinicalTrials


class LookupsController(object):
    '''
    This class contains methods for simple lookups such as gene name lookup etc.
    '''
    
    @cherrypy.expose
    def autocomplete_gene_symbol(self, term):
        #results = Hgnc.search(term)
        json_obj = []
        for result in Hgnc.search(term):
            #json_obj.append(result.get("gene").symbol + " (" + result.get("close_match") + ")")
            #json_obj.append({"id" : result.get("gene")._id, "text" : result.get("gene").symbol + " (" + result.get("close_match") + ")"})  
            json_obj.append({"value" : "<span class='rounded-corner-label label-genes'>"+result.get("match").symbol+"</span>&nbsp;", 
                             "label" : result.get("match").symbol + " (" + result.get("close_match") + ")"})      
        
        for result in Medic.search(term):
            json_obj.append({"value" : "<span class='rounded-corner-label label-diseases'>"+result.get("match").get_disease_name()+"</span>&nbsp;", 
                             "label" : result.get("match").get_disease_name() + " (" + result.get("close_match") + ")"})
        
        return json.dumps(json_obj)
    
    @cherrypy.expose
    def validate_trial_ids(self, q, _):
        ct = ClinicalTrials()
        trial_ids = ct.search(q)
        print "Trial IDs are: "+str(trial_ids)
        
        if(len(trial_ids) > 0):
            return json.dumps([{"id":trial_id, "text":trial_id} for trial_id in trial_ids])
        
        else:
            return json.dumps([])
    
    @cherrypy.expose
    def autocomplete_disease_name(self, term):
        #cancers = [{"label":"Breast Cancer", "value":1}, {"label":"Colon Cancer", "value":2} ]
        medic_diseases = Medic.search(term)
        jsonobj = []
        for entry in medic_diseases:
            disease = entry["match"]
            jsonobj.append({ "value" : disease.get_disease_id(), "label" : disease.get_disease_name() })
        print jsonobj
        return json.dumps(jsonobj)
    
    @cherrypy.expose
    def autocomplete_drug_names(self, term):
        drugs = Drug.lookup_by_name(term)
        drugs.sort(key=lambda k: difflib.SequenceMatcher(None, term, k.name).ratio())

        close_matches = [{"value":drug.ids["DRUGBANK"], "label":drug.name} for drug in drugs[:5]]
        print "drug matches: "+str(close_matches)
        return json.dumps(close_matches)
        