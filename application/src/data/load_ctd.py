'''
Created on Aug 13, 2014

@author: varun
'''

from db.other.medic import Medic


dir_name = "/Users/varun/Downloads/biomedical/"

def main():
    load_diseases()

def load_diseases():
    f = open(dir_name + "CTD_diseases.tsv", "r")
    count = 0
    total_count = 0
    
    for raw in f:
        if raw[0] != "#":
            line = raw.split("\t")
            disease_name = line[0].strip()
            disease_id = line[1].strip()[5:]
            alt_disease_ids = [a.strip()[5:] for a in line[2].strip().split("|")]
            definition = line[3].strip()
            parent_ids = [a.strip()[5:] for a in line[4].strip().split("|")]
            synonyms = [a.strip() for a in line[2].strip().split("|")]
            
            medic = Medic()
            medic.set_disease_id(disease_id)
            medic.set_disease_name(disease_name)
            medic.set_alt_disease_ids(alt_disease_ids)
            medic.set_disease_definition(definition)
            medic.set_parent_ids(parent_ids)
            medic.set_disease_synonyms(synonyms)
            
            if(medic.save()):
                count += 1
                total_count += 1
                if count == 1000:
                    count = 0
                    print "Processed 1000 records, current total: {}".format(str(total_count))
                
    print "Done"
    print "{} lines processed".format(str(total_count))
    f.close()

if __name__ == '__main__':
    main()