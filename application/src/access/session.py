'''
Created on Sep 23, 2014

@author: varun
'''
from cherrypy.lib import sessions
from cherrypy.lib.sessions import RamSession
from cherrypy._cpcompat import copyitems

from config import get_cache_connection

class BiocustomSession(sessions.RamSession):
    '''
    This is a custom session implementation for this project.
    At this point, we do some extra clean-up on session expiration.
    In future we may want to store session in Mongo
    '''
    #cache = {}
    #locks = {}

    def __init__(self, session_id = None, **kwargs):
        '''
        Constructor
        '''
        RamSession.__init__(self, id = session_id, **kwargs)
        
    def clean_up(self):
        #sessions.RamSession.clean_up(self)
        print "Cache cleanup started....."
        external_cache = get_cache_connection()
        print "self is: "+str(dict(self))
        print "cache is: "+str(self.cache)
        
        now = self.now()
        for session_id, (data, expiration_time) in copyitems(self.cache):
            if expiration_time <= now:
                try:
                    query_keys = data.get("query_keys")
                    if query_keys and len(query_keys) > 0:
                        print "Session: "+str(session_id)+" has expired"
                        print "Deleting keys: "+str(query_keys)
                        external_cache.delete(*query_keys)
                        print "Deleted"
                    print "Cache cleanup done"                    
                    del self.cache[session_id]
                except KeyError:
                    pass
                try:
                    del self.locks[session_id]
                except KeyError:
                    pass
        
        # added to remove obsolete lock objects
        for session_id in list(self.locks):
            if session_id not in self.cache:
                self.locks.pop(session_id, None)        
        