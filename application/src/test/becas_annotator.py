'''
Created on Apr 11, 2014

@author: varun
'''
import becas


def main():
    becas.email = "vs454@georgetown.edu"
    #becas.tool = "test"
    text = '''
    The concentration of alpha 2-macroglobulin, alpha 1-antitrypsin, plasminogen, C3-complement, fibrinogen degradation products (FDP) and fibrinolytic activity, were studied in the aqueous humour and serum from nine patients with Fuchs' endothelial dystrophy, 17 patients with uncomplicated senile cataract and in the secondary aqueous from six cataract patients.
    '''
    #results = becas.annotate_text(text, groups = {"PRGE":True})
    pubmed_id = 23924853
    json_results = becas.export_text(text, 'json')
    results = becas.annotate_publication(pubmed_id)
    print results.keys()
    for key, value in results.iteritems():
        print "{} - {}".format(key, str(value))
    #print results["entities_title"]
    #print results["ids"]["UNIPROT:P48736:T116:PRGE"]


if __name__ == '__main__':
    main()