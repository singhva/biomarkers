'''
Created on Jun 20, 2014

@author: varun
'''
import json
import os
from os.path import dirname

import cherrypy
from mako.lookup import TemplateLookup

from config import get_cache_connection
from config import get_db_connection
from misc import utils
from db.ncbi.pubmed import Pubmed
from services.pubmed_service import PubmedService
from nlp.annotations import Annotation, ManualAnnotations


current_dir = dirname(os.path.abspath(__file__))
application_dir = dirname(current_dir)
lookup = TemplateLookup(directories=[application_dir+'/html/'])

class PubmedController(object):
    
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.service = PubmedService()
        
    @cherrypy.expose
    def search(self, term, **kwargs):
        session = getattr(cherrypy, 'session')
        cache = get_cache_connection()
        db = get_db_connection()
        pagenum = self.service.get_page_num(kwargs.get("move"), int(kwargs.get("pagenum", 1)))
        query_key = kwargs.get("query_key")
        basic_cache_key = ""
        exact_cache_key = ""
            
        if (query_key is None) or (query_key == ""):
            print "Query key doesn't exist"
            new_query_key = utils.create_random_string()
            term = term.strip()
            if utils.is_pubmed_list(term):
                print "Term only contains Pubmed IDs"
                ids = [temp.strip() for temp in term.split(",")]
                sorted_useful_publications = Pubmed.get_publications_from_pmids(ids)
                self.service.cache_session_publication_ids(new_query_key, sorted_useful_publications)
                
            else:
                exact_cache_key = utils.create_pubmed_exact_cache_key(term, **kwargs)
                basic_cache_key = utils.create_pubmed_basic_cache_key(term)  
                if cache.exists(exact_cache_key):
                    print "Exact cache exists"
                    sorted_useful_publications = self.service.lookup_cache_key(exact_cache_key, 0, -1)
                    self.service.cache_session_publication_ids(new_query_key, sorted_useful_publications)
                    
                elif cache.exists(basic_cache_key):
                    print "Retrieving basic variant from cache...."
                    publications = self.service.lookup_cache_key(basic_cache_key, 0, -1)
                    filtered_useful_publications = self.service.filter(publications, kwargs.get("filter"))
                    sorted_useful_publications = self.service.sort(filtered_useful_publications, kwargs.get("sort_key"))                
                    self.service.cache_global_search_publication_ids(exact_cache_key, sorted_useful_publications)
                    self.service.cache_session_publication_ids(new_query_key, sorted_useful_publications)
                    
                else:                   
                    search_term = utils.create_pubmed_search(term, **kwargs)
                    print "No cached value found... searching pubmed"
                    search_result = Pubmed.search(search_term, retstart = 0, retmax = Pubmed.RETMAX, usehistory = 'y')
                    annotations = db["ANNOTATIONS"].find( {"PMID": {"$in" : search_result["IdList"]} })                       
                    useful_pmids = [ annotation["PMID"] for annotation in annotations if annotation.get("GENE")] # Add other annotations
                    
                    useful_publications = Pubmed.get_publications_from_pmids(useful_pmids)
                    self.service.cache_global_search_publication_ids(basic_cache_key, useful_publications)                                           
                    filtered_useful_publications = self.service.filter(useful_publications, kwargs.get("filter"))
                    sorted_useful_publications = self.service.sort(filtered_useful_publications, kwargs.get("sort_key"))  
                    if basic_cache_key != exact_cache_key:
                        self.service.cache_global_search_publication_ids(exact_cache_key, sorted_useful_publications)
                    self.service.cache_session_publication_ids(new_query_key, sorted_useful_publications)
                    
            session["query_keys"].append(new_query_key)
            jsonobj = self.service.process_results_from_cache(new_query_key, pagenum)
            jsonobj["query_key"] = new_query_key
            query_key = new_query_key
            if kwargs.get("get_filters") == "yes":
                jsonobj["filters"] = self.service.get_filters(sorted_useful_publications)
            
        else:
            print "Query key exists"
            jsonobj = self.service.process_results_from_cache(query_key, pagenum)                           
                
        '''                                
            if web_env:
                print "Search history found, key is: " + web_env
                result = Pubmed.search(term, sort = kwargs.get("sort_key", ""), retstart = retstart, retmax = retmax, WebEnv = web_env, usehistory = 'y')
            else:
                result = Pubmed.search(term, sort = kwargs.get("sort_key", ""), retstart = retstart, retmax = retmax, usehistory = 'y')
                session["query_cache"][term] = result["WebEnv"]
                print "No history found... setting WebEnv to: " + result["WebEnv"]                       
        '''
        
        #cache.release()
        return json.dumps(jsonobj)            
        
    
    @cherrypy.expose
    def get(self, **kwargs):
        session = getattr(cherrypy, 'session')
        query_key = kwargs.get("query_key")
        pagenum = self.service.get_page_num(kwargs.get("move"), int(kwargs.get("pagenum", 1)))
        jsonobj = {}
        
        if (query_key is None) or (query_key == ""):
            print "Query key doesn't exist"
            pmids = kwargs.get("selected_pmids").split("|")
            new_query_key = utils.create_random_string()    
            publications = Pubmed.get_publications_from_pmids(pmids)
            self.service.cache_session_publication_ids(new_query_key, publications)
            session["query_keys"].append(new_query_key)
            jsonobj = self.service.process_results_from_cache(new_query_key, pagenum)
            jsonobj["query_key"] = new_query_key
            query_key = new_query_key
            
        else:
            print "Query key exists"
            jsonobj = self.service.process_results_from_cache(query_key, pagenum)
            
        if kwargs.get("get_filters", "yes") == "yes":
            jsonobj["filters"] = self.service.get_filters(query_key) 
        
        return json.dumps(jsonobj) 
       
    
    @cherrypy.expose
    def dbsearch(self, term):
        results = utils.search_marker(term)
        print results
        return json.dumps(results)
    
    @cherrypy.expose
    def save_pdf(self, pubmed_id = '0'):
        print "Got request to save pdf. Pubmed ID: " + pubmed_id
        return "saved"
    
    '''
    @cherrypy.expose
    def get_drug_gene_publications(self, drug_id, gene_sym):
        results = Pubmed.get_publications_from_database(drug_id, gene_sym)
        print results
        return json.dumps(results)
    '''
    
    @cherrypy.expose
    def analyze_publication(self, pmid):
        analysis = self.service.get_interesting_stuff(pmid)
        return json.dumps(analysis)
        
    @cherrypy.expose
    def save_curated_publication(self, json_string):
        publication = json.loads(json_string);
        print publication
        
        return "Thanks"
    
    @cherrypy.expose
    def save_disease_annotation(self, pmid, original_text, db_id, start_pos, end_pos):
        manual_annotations = ManualAnnotations.get_by_pmid(pmid)
        if manual_annotations.create_or_update_disease_annotation(original_text, db_id, start_pos, end_pos):
            return
        
        else:
            raise cherrypy.HTTPError(status=500, message=None)
        