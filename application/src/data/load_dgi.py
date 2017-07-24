'''
Created on Apr 15, 2014

@author: varun
'''

import re
import urllib2

import lxml.html
from pymongo import Connection
from db.other.schema import drugbank


DB_NAME = "BIOMARKERS"
FOLDER_NAME = "/Users/varun/Desktop/Cancer_Biomarkers"

def main():
    connection = Connection('localhost', 27017)
    db = connection[DB_NAME]
    #load_marker_list(db)
    #load_drugbank_drugs(db)
    #load_drugbank_interactions(db)
    #print get_drugbank_citations("DB00001","54")
    load_drugbank_citations(db)
    connection.close()
    
def load_marker_list(db):
    markers_file = open("{}/markers.tsv".format(FOLDER_NAME))
    #db["GENES"].create_index("gene.sym", unique=True)
    count = 0
    for line in markers_file:
        gene = line.strip()
        print "Gene is: "+gene
        #record = {"gene":{"sym":gene}}
        record = {"_id":gene}
        if db["GENES"].save(record) is not None:
            count += 1
        
    print "Total inserted = "+str(count)
    markers_file.close()
    
def load_drugbank_xml_pyxb(db): #NOT NEEDED
    f = open("{}/DataSets/drugbank.xml".format(FOLDER_NAME))
    print "reading xml... ",
    xml = urllib2.urlopen("file://{}/DataSets/drugbank.xml".format(FOLDER_NAME)).read()
    print "read"
    #doc = domutils.StringToDOM(xml)
    fc_return = drugbank.CreateFromDocument(xml)
    #fc_return = drugbank.CreateFromDOM(doc.documentElement)
    if fc_return.Success:
        drugs = fc_return.drugs
        print len(drugs)
    f.close()
    
def get_drugbank_citations(drug_id, gene_partner_id):
    BASE_URL = "http://v3.drugbank.ca/drugs"
    URL = BASE_URL+"/"+drug_id
    
    html = urllib2.urlopen(URL).read()
    html = lxml.html.fromstring(html)
    targets_table = html.get_element_by_id("targets")
    gene_div = targets_table.get_element_by_id("target-"+gene_partner_id)
    citations_span = gene_div.find_class("citations")[0]
    pubmed_ids = []
    for link in lxml.html.iterlinks(citations_span):
        #print link[2]
        pubmed_ids.append(re.search("[0-9]+", link[2]).group(0))
    
    return pubmed_ids
    
def load_drugbank_drugs(db):
    drugs_file = open("{}/DataSets/DGI/druggable_gene_tsvs/DrugBank_WashU_DRUGS.tsv".format(FOLDER_NAME))
    count = 0
    headers = []
    for i, line in enumerate(drugs_file):
        line = line.strip().split("\t")
        if i == 0:
            headers = line
            print "Headers are: "+str(headers)
            
        else:
            values = dict(zip(headers, line))
            drug_id = values.get("drug_id","").strip()
            drug_name = values.get("drug_name","").strip()
            drug_synonyms = [syn.strip() for syn in values.get("drug_synonyms","").strip().split(",")]
            drug_cas_number = values.get("drug_cas_number","").strip()
            drug_brands = [brand.strip() for brand in values.get("drug_brands","").strip().split(",")]
            drug_type = values.get("drug_type","").strip()
            drug_groups = [group.strip() for group in values.get("drug_groups","").strip().split(",")]
            drug_categories = [category.strip() for category in values.get("drug_categories","").strip().split(",")]
            drug = {"DB":"DRUGBANK","DB_ID":drug_id,"NAME":drug_name,"SYNS":drug_synonyms,"CAS_NUMBER":drug_cas_number,"BRANDS":drug_brands,"TYPE":drug_type\
                    ,"GROUPS":drug_groups,"CATEGORIES":drug_categories}
            db["DRUGS"].save(drug)
            count += 1
            
    print "Saved {} drugs from Drugbank".format(str(count))
    drugs_file.close()
    
def load_drugbank_interactions(db):
    interactions_file = open("{}/DataSets/DGI/druggable_gene_tsvs/DrugBank_WashU_INTERACTIONS.tsv".format(FOLDER_NAME))
    uniprot_regex="([A-NR-Z][0-9][A-Z][A-Z0-9][A-Z0-9][0-9])|([OPQ][0-9][A-Z0-9][A-Z0-9][A-Z0-9][0-9])"
    count = 0
    headers = []
    for i, line in enumerate(interactions_file):
        line = line.strip().split("\t")
        if i == 0:
            headers = line
            print "headers is: "+str(headers)
        else:
            values = dict(zip(headers, line))
            gene_symbol = values.get("gene_symbol","").strip()
            drug_id = values.get("drug_id","").strip()
            gene = db["GENES"].find_one({"_id":gene_symbol})
            drug = db["DRUGS"].find_one({"DB":"DRUGBANK","DRUG_ID":drug_id})
            interaction = None
            if gene is not None and (drug is not None):
                interaction = db["INTERACTIONS"].find_one({"GENE_SYM":gene_symbol,"DRUG_ID":drug["_id"]})
                if gene.get("UNIPROT_ID") is None and re.match(uniprot_regex,values.get("uniprot_id","")):
                    gene["UNIPROT_ID"] = re.match(uniprot_regex,values.get("uniprot_id")).group(0)
                if gene.get("ENTREZ_ID") is None and re.match("[0-9]+",values.get("entrez_id","")):
                    gene["ENTREZ_ID"] = re.match("[0-9]+",values.get("entrez_id")).group(0)
                db["GENES"].save(gene)

                if interaction is None:
                    interaction = {"GENE_SYM":gene_symbol,"DRUG_ID":drug["_id"]}
                    interaction["ACTIONS"] = [action.strip() for action in values["target_actions"].strip().split(",")]
                    interaction["GENE_PARTNER_ID"] = values.get("partner_id")
                    
                    print "Inserting: {} - {} interaction".format(gene_symbol, drug["NAME"])
                    db["INTERACTIONS"].save(interaction)
                    count += 1
                
    print "{} interactions saved".format(count)
    interactions_file.close()
    
def load_drugbank_citations(db):
    interactions = db["INTERACTIONS"].find({"GENE_SYM":"ERBB2"})
    for interaction in interactions:
        gene_partner_id = interaction["GENE_PARTNER_ID"]
        drugbank_id = db["DRUGS"].find_one({"_id":interaction["DRUG_ID"]})["DB_ID"]
        pubmed_ids = get_drugbank_citations(drugbank_id, gene_partner_id)
        interaction["PUBLICATIONS"] = []
        for pmid in pubmed_ids:
            interaction["PUBLICATIONS"].append({"PMID":pmid})
            
        db["INTERACTIONS"].save(interaction)
        print interaction
    
if __name__ == '__main__':
    main()