'''
Created on Apr 29, 2014

@author: varun
'''
import datetime
import urllib2

from data import get_db_connection


def main():
    print "Downloading file.... ",
    infile = download_file()
    print "Done"
    process(infile)

def download_file():
    output_dir = "/Users/varun/Desktop/Cancer_Biomarkers/DataSets/HGNC"
    base_url = "http://www.genenames.org/cgi-bin/download"
    url = base_url+"?col=gd_hgnc_id&col=gd_app_sym&col=gd_app_name&col=gd_status&col=gd_locus_type&col=gd_locus_group&col=gd_prev_sym&col=gd_aliases&col=gd_pub_chrom_map&col=gd_gene_fam_name&col=md_eg_id&col=md_prot_id&status=Approved&status_opt=2&where=&order_by=gd_hgnc_id&format=text&limit=&submit=submit"
    infile = urllib2.urlopen(url, None, 120)
    output = open(output_dir+"/hgnc_"+str(datetime.date.today())+".txt",'wb')
    output.write(infile.read())
    output.close()
    return output.name

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
            hgnc_id = values.get("HGNC ID","").strip()
            approved_symbol = values.get("Approved Symbol","").strip()
            approved_name = values.get("Approved Name","").strip()
            status = values.get("Status", "").strip()
            locus_type = values.get("Locus Type", "").strip()
            locus_group = values.get("Locus Group", "").strip()
            previous_symbols = values.get("Previous Symbols", "").strip()
            synonyms = [x.strip() for x in values.get("Synonyms", "").strip().split(",")]
            chromosome = values.get("Chromosome","").strip()
            gene_family_tag = values.get("Gene Family Tag","").strip()
            entrez_id = values.get("Entrez Gene ID(supplied by NCBI)","").strip()
            uniprot_id = values.get("UniProt ID(supplied by UniProt)", "").strip()
            
            entry = {"_id":hgnc_id, "SYMBOL":approved_symbol, "NAME":approved_name, "STATUS":status, "LOCUS_TYPE":locus_type, \
                     "LOCUS_GROUP":locus_group, "PREV_SYMBOLS":previous_symbols, "SYNS":synonyms, "CHR":chromosome, "TAG":gene_family_tag, "ENTREZ_ID":entrez_id, "UNIPROT_ID":uniprot_id}
            print "Processing: "+approved_symbol
            db["HGNC"].save(entry)
            
    infile.close()

if __name__ == '__main__':
    main()