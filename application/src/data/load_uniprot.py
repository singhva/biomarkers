'''
Created on Apr 30, 2014

@author: varun
'''
from data import get_db_connection


def main():
    #infile = download_file()
    infile = "/Users/varun/Desktop/Cancer_Biomarkers/DataSets/UNIPROT/mart_export_04-30-2014.txt"
    process(infile)  
    
def download_file():
    pass
    
def process(file_name):
    infile = open(file_name,"r")
    db =  get_db_connection()
    headers = []
    for i, line in enumerate(infile):
        line = line.strip().split("\t")
        if i == 0:
            headers = line
            
        else:
            values = dict(zip(headers, line))
            uniprot_id = values.get("Accession", "").strip()
            uniprot_name = values.get("Entry name", "").strip()
            protein_name = values.get("Protein name", "").strip()
            gene_name = values.get("Gene name", "").strip()
            status = values.get("Status", "").strip()
            entry = {"_id":uniprot_id, "ENTRY_NAME":uniprot_name, "PROTEIN_NAME":protein_name, "GENE_NAME":gene_name, "STATUS":status}
            print "Processing: "+uniprot_id
            db["UNIPROT"].save(entry)
    
    infile.close()

if __name__ == '__main__':
    main()
