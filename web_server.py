'''
Created on Apr 18, 2014

@author: varun
'''
import os, sys
current_dir = os.path.abspath(".")
sys.path.append(current_dir + "/application/src/")
import cherrypy
from mako.lookup import TemplateLookup
from controllers.pubmed_controller import PubmedController
from controllers.lookups_controller import LookupsController
from access.auth import AuthController, require
import argparse
from cherrypy.process.plugins import Daemonizer
from cherrypy.lib import sessions
from access.session import BiocustomSession
import config

lookup = TemplateLookup(directories=[current_dir+'/application/html'])

class BioMarkers(object):
    '''
    classdocs
    '''
    
    _cp_config = {

    }
    
    def __init__(self):
        sessions.BiocustomSession = BiocustomSession
        #handlers.TimedRotatingFileHandler("", when='midnight')
        config.configure()
        self.pubmed = PubmedController()
        self.lookups = LookupsController()
        self.auth = AuthController()
    
    @cherrypy.expose
    @require()
    def index(self):
        tmpl = lookup.get_template("index.html")
        cancers = {"breast":"Breast Cancer", "colon":"Colon Cancer"}
        trial_types = {"ct":"Clinical Trial", "phase1":"Clinical Trial, Phase I", "phase2":"Clinical Trial, Phase II" \
        , "phase3":"Clinical Trial, Phase III", "phase4":"Clinical Trial, Phase IV", "pragmatic":"Pragmatic Clinical Trial", "randomized":"Randomized Controlled Trial"}
        print "base is: "+cherrypy.request.base
        return tmpl.render(cancers=cancers, trial_types=trial_types)
        
def start_standalone(env):
    cherrypy.config.update(current_dir + "/application/{}.ini".format(env))
    biomarkers = BioMarkers()
    
    if env == "prod":
        Daemonizer(cherrypy.engine).subscribe()
    
    cherrypy.tree.mount(biomarkers, "/biomarkers", config = current_dir + "/application/common.ini")
    cherrypy.engine.start()
    cherrypy.engine.block()    

if __name__ == '__main__':    
    parser = argparse.ArgumentParser(description='Start cherrypy Biomarkers server')
    parser.add_argument("--env", dest="environment", help="Name of environment ('dev' for development, 'prod' for production)")
    args = parser.parse_args()
    
    if not args.environment:
        parser.print_help()
    else: 
        start_standalone(args.environment)
