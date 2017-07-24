'''
Created on Dec 17, 2013

@author: varun
'''
from clinicaltrials import ClinicalTrials


def main():
    ct = ClinicalTrials()
    study_ids = ct.search("drug", "children's oncology group")
    cogid_map = ct.find_cog_protocols(study_ids)
    ct.writeToCsv(cogid_map)


if __name__ == '__main__':
    main()