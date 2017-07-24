'''
Created on Apr 17, 2014

@author: varun
'''
import datetime
import random
import string
import re
from types import ListType, StringType, UnicodeType

from config import get_db_connection


def parse_pubmed_abstract(text, gene_syms):
    genes = "|".join(["{}".format(sym) for sym in gene_syms])
    status_regex = "(?P<name>{})".format(genes)
    status_regex += "[-\s]?(?P<expr>negative|positive|express|overexpress|underexpress|amplif|coamplif|aberrat|delet)(?P<suffix>:ing|ion|ied|ication)?"
    for match in re.finditer(status_regex, text):
        print match.group("expr")
       
''' 
def get_interactions_from_pubmed(marker):
    output = {"marker_name":marker, "agent_associations":[]}
    db = get_db_connection()
    interactions = db["INTERACTIONS"].find({"GENE_SYM":marker})
    for interaction in interactions:
        drug = db["DRUGS"].find_one({"_id":interaction["DRUG_ID"]})
        term = create_pubmed_search("HER2[All Fields]")
        pmids = Pubmed().search(term)["IdList"]
        output["agent_associations"].append({"name":drug["NAME"], "publications":Pubmed.get_interesting_stuff(pmids)})
        
    return output


def get_publications_from_database(drug_id, gene_sym):
    db = get_db_connection()
    interaction = db["INTERACTIONS"].find_one({"GENE_SYM":gene_sym, "DRUG_ID":ObjectId(drug_id)})
    ret_value = [publication["PMID"] for publication in interaction.get("PUBLICATIONS")]
    return Pubmed().get_publications_from_ids(ret_value) # *** CHANGE THIS ****
    
'''

def search_marker(term):
    ret_value = {}
    db = get_db_connection()
    interactions = db["INTERACTIONS"].find({"GENE_SYM": {"$regex": term+"[0-9a-zA-Z]*", '$options': 'i'}})
    for interaction in interactions:
        drug = db["DRUGS"].find_one({"_id": interaction["DRUG_ID"]})
        gene_sym = interaction["GENE_SYM"]
        value = ret_value.get(gene_sym, [])
        value.append({"drug_id":str(drug["_id"]), "drug_name":drug["NAME"], "drug_actions":interaction["ACTIONS"]})
        ret_value[gene_sym] = value
    return ret_value

def create_pubmed_search(term, **kwargs):
    cur_date = datetime.date.today()
    ten_years_ago = cur_date - datetime.timedelta(days = 365 * 10)
    #term = '({}) AND Clinical Trial[ptyp] AND ("{}"[PDat] : "{}"[PDat]) AND "humans"[MeSH Terms] '.format(term, str(ten_years_ago).replace("-", "/"), str(cur_date).replace("-", "/"))
    term = '({}) AND Clinical Trial[ptyp] AND "humans"[MeSH Terms] '.format(term, str(ten_years_ago).replace("-", "/"), str(cur_date).replace("-", "/"))
    #term += "AND jsubsetaim[text])"
    if kwargs.get("with_trials_only"):
        term += "AND clinicaltrials.gov [si] "
    print "term is: "+term
    return term

def create_pubmed_exact_cache_key(term, **kwargs):
    cache_key = "TERM:"+term.lower()
    if type(kwargs.get("sort_key")) in [UnicodeType, StringType]:
        cache_key += '|SORT_BY:'+kwargs.get("sort_key")
        
    if kwargs.get("filter", "") != "":
        filter_map = get_filter_map(kwargs.get("filter"))
        for filter_key, filter_value in filter_map.iteritems():
            cache_key += "|FILTER_KEY:" + filter_key
            cache_key += "|FILTER_VALUE:" + ",".join(sorted(filter_value))
        '''
        filter_key, filter_value = get_filter(kwargs.get("filter"))
        print "filters obtained from get_filter are: {}, {}".format(filter_key, filter_value)
        key += "|FILTER_KEY:" + filter_key
        key += "|FILTER_VALUE:" + filter_value
        '''
    print "Exact key is: "+cache_key
    return cache_key

def get_filter_map(filters):
    filter_map = {}
    
    if type(filters) in [UnicodeType, StringType]:
        if filters != "":  
            filter_key, filter_value = get_filter(filters)
            filter_map[filter_key] = [filter_value.lower()]
        print "filter map is: "+str(filter_map)
        
    elif type(filters) is ListType:
        for filter_text in filters:
            filter_key, filter_value = get_filter(filter_text)
            print "key: {}, value: {}".format(filter_key, filter_value)
            if filter_map.get(filter_key):
                filter_map.get(filter_key).append(filter_value.lower())
            else:
                filter_map[filter_key] = [filter_value.lower()]
            
        print "filter map is: "+str(filter_map)
        
    else:
        print "Incorrect filter found"
        
    return filter_map

def get_filter(filter_text):
    filter_key_value = filter_text.split(":")
    print "filter_key_value is: "+str(filter_key_value)
    if len(filter_key_value) == 2:
        filter_key = filter_key_value[0]
        filter_value = filter_key_value[1]
        
        return (filter_key, filter_value)
    
    else:
        return ("", "")
    
def is_pubmed_list(input_text):
    split_text = input_text.split(",")
    contains_numbers_only = [text.strip().isdigit() for text in split_text]
    print "inside is_pubmed_list: "+str(contains_numbers_only)
    
    return False not in contains_numbers_only

def create_pubmed_basic_cache_key(term):
    key = "TERM:"+term.lower()
        
    return key

def create_random_string():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
            