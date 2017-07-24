'''
Created on Aug 1, 2014

@author: varun
'''
from config import get_db_connection


dir_name = "/Users/varun/Downloads/biomedical/"
#dir_name = "/home/ubuntu/downloads/"

def main():
    #load_gene_annotations()
    load_disease_annotations()
    
def transfer_annotations_to_pubmed():
    db = get_db_connection()
    for entry in db["ANNOTATIONS"].find():
        pmid = entry["PMID"]
        pubmed = {"PMID" : pmid, "RAW" : {}, "ANNOTATIONS" : {}}
    
def load_disease_annotations():
    f = open(dir_name + "disease2pubtator", "r")
    db = get_db_connection()
    count = 0
    net = 0
    total_count = 0
    print "Processing......"
    prev_id = None
    obj = None
    
    for raw in f:
        line = raw.split("\t")
        if line[0].isdigit():
            pmid = line[0].strip()
            mesh_id = line[1].strip()
            if pmid == prev_id:
                entry = obj
                temp = entry["DISEASE"].get(mesh_id)
                if temp:
                    temp["MENTIONS"].extend(line[-1].strip().split("|"))
                else:
                    entry["DISEASE"][mesh_id] = {"MENTIONS" : line[-1].strip().split("|")}
                    
            else:
                if obj:
                    if not db["ANNOTATIONS"].find_and_modify(
                                                       query = {"PMID" : obj.get("PMID")},
                                                       update = { "$set" : {"PMID" : obj.get("PMID"), "DISEASE" : obj.get("DISEASE")} },
                                                       upsert = False
                                                      ):
                        db["ANNOTATIONS"].save(obj)
                    net += 1
                entry = {}
                entry["PMID"] = pmid
                entry["DISEASE"] = {mesh_id : {"MENTIONS" : line[-1].strip().split("|")} }
                obj = entry
                prev_id = pmid   
                
            count += 1
            total_count += 1
            if count == 1000:
                count = 0
                print "Processed 1000 records, total: {}".format(total_count)
    
    print "Done"
    print "{} lines processed".format(str(total_count))
    print "{} pmids added".format(str(net))
    f.close()            
                

def load_gene_annotations():
    f = open(dir_name + "gene2pubtator", "r")
    db =  get_db_connection()
    count = 0
    net = 0
    total_count = 0
    #pmids = set()
    print "Processing....."
    prev_id = None
    obj = None
    
    for raw in f:
        line = raw.split("\t")
        if line[0].isdigit():
            pmid = line[0].strip()
            entrez_id = line[1].strip()
            #entry = db["ANNOTATIONS"].find_one({"PMID" : pmid}) if (pmid in pmids) else None
            if pmid == prev_id:
                entry = obj
                temp = entry["GENE"].get(entrez_id)
                if temp:                   
                    temp["MENTIONS"].extend(line[-1].strip().split("|"))
                else:
                    entry["GENE"][entrez_id] = {"MENTIONS" : line[-1].strip().split("|")}
            else:
                if obj:
                    db["ANNOTATIONS"].save(obj)
                    net += 1
                entry = {}
                entry["PMID"] = pmid
                entry["GENE"] = {entrez_id : {"MENTIONS" : line[-1].strip().split("|")} }
                obj = entry
                prev_id = pmid
                    
                
            #pmids.add(pmid)                    
            count += 1
            total_count += 1
            if count == 1000:
                count = 0
                print "Processed 1000 records"
    
    print "Done"
    print "{} lines processed".format(str(total_count))
    print "{} pmids added".format(str(net))
    f.close()

if __name__ == '__main__':
    main()