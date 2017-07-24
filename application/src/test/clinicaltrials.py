'''
Created on May 14, 2014

@author: varun
'''

from ncbi.clinicaltrials import ClinicalTrials, ClinicalStudy


def main():
    #ct = ClinicalTrials()
    #print ct.get_search_results_count("HER2", rslt="With")
    #print ct.get_marker_search_results_count("HER2")
    cs = ClinicalStudy("NCT01014286")
    cs.get()
    print cs.get_title()
    print cs.get_phase()
    print cs.get_enrolled_patients_count()
    print cs.get_drugs()
    '''
    directory = "/Users/varun/Desktop/Cancer_Biomarkers"
    outfile = open(directory+"/clinical_trials_search_results.tsv","w")
    outfile.write("Symbol\tExpanded\tCount\n")
    with open(directory+"/all_markers.txt") as f:
        for line in f:
            results = ct.get_marker_search_results(line.strip())
            print "{}\t{}\t{}\n".format(line.strip(), results[0], str(results[1]))
            outfile.write("{}\t{}\t{}\n".format(line.strip(), results[0], str(results[1])))
            
    outfile.close()
    '''
    #gene = Utils.search_gene_names("HER2")
    #print Utils.get_all_gene_ids(gene[0].get("SYMBOL"))

if __name__ == '__main__':
    main()