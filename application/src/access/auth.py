'''
Created on May 27, 2014

@author: varun
'''

import md5
import os
from os.path import dirname
import urllib
from user import User
import cherrypy
from mako.lookup import TemplateLookup
from config import get_cache_connection


SESSION_KEY = '_cp_username'

current_dir = dirname(os.path.abspath(__file__))
application_dir = dirname(dirname(current_dir))
lookup = TemplateLookup(directories=[application_dir+'/html/auth', application_dir+'/html/'])

def check_credentials(username, password):
    """Verifies credentials for username and password.
    Returns None on success or a string describing the error on failure"""

    user = User.get_by_username(username.strip())
    if user is not None:
        if user.password == md5.new(password).hexdigest(): return None
        else: return u"Incorrect username or password."
        
    else:
        return u"Enter a valid username"

def check_auth(*args, **kwargs):
    """A tool that looks in config for 'auth.require'. If found and it
    is not None, a login is required and the entry is evaluated as a list of
    conditions that the user must fulfill"""
    conditions = cherrypy.request.config.get('auth.require', None)
    get_params = urllib.quote(cherrypy.request.request_line.split()[1])
    login_url = cherrypy.config["app.base_url"] + "/auth/login"
    session = getattr(cherrypy, 'session')
    #print "Sessions are: ",
    #print dir(cherrypy.serving.session)
    #print "keys: "+str(cherrypy.serving.session.cache)
    #print session._get_dict()
    if conditions is not None:
        username = session.get(SESSION_KEY)
        if username:
            cherrypy.request.login = username
            for condition in conditions:
                # A condition is just a callable that returns true or false
                if not condition():
                    raise cherrypy.HTTPRedirect(login_url+"?from_page={}".format(get_params))
        else:
            raise cherrypy.HTTPRedirect(login_url+"?from_page={}".format(get_params))
        
    else:
        username = session.get(SESSION_KEY)
        cherrypy.request.login = username
    
cherrypy.tools.auth = cherrypy.Tool('before_handler', check_auth)

def require(*conditions):
    """A decorator that appends conditions to the auth.require config
    variable."""
    def decorate(f):
        if not hasattr(f, '_cp_config'):
            f._cp_config = dict()
        if 'auth.require' not in f._cp_config:
            f._cp_config['auth.require'] = []
        f._cp_config['auth.require'].extend(conditions)
        return f
    return decorate


# Conditions are callables that return True
# if the user fulfills the conditions they define, False otherwise
#
# They can access the current username as cherrypy.request.login
#
# Define those at will however suits the application.

def member_of(groupname):
    def check():
        # replace with actual check if <username> is in <groupname>
        return cherrypy.request.login == 'joe' and groupname == 'admin'
    return check

def name_is(reqd_username):
    return lambda: reqd_username == cherrypy.request.login

# These might be handy

def any_of(*conditions):
    """Returns True if any of the conditions match"""
    def check():
        for c in conditions:
            if c():
                return True
        return False
    return check

# By default all conditions are required, but this might still be
# needed if you want to use it inside of an any_of(...) condition
def all_of(*conditions):
    """Returns True if all of the conditions match"""
    def check():
        for c in conditions:
            if not c():
                return False
        return True
    return check


# Controller to provide login and logout actions

class AuthController(object):
    
    def on_login(self, username):
        """Called on successful login"""
        print "inside on_login"
        print "setting cache...."
        session = getattr(cherrypy, 'session')
        session["query_keys"] = []
    
    def on_logout(self, username):
        """Called on logout"""
        cache = get_cache_connection()
        session = getattr(cherrypy, 'session')
        if len(session["query_keys"]) > 0:
            print "Deleting keys: "+str(session["query_keys"])
            cache.delete(*session["query_keys"])
            print "Deleted"
    
    def get_loginform(self, username, msg = None, from_page=None):
        print "application_dir is: "+application_dir
        tmpl = lookup.get_template("login.html")
        return tmpl.render(msg = msg or "", from_page=from_page or cherrypy.config["app.base_url"])
    
    @cherrypy.expose
    def login(self, username=None, password=None, from_page=None):
        if username is None or password is None:
            print "username or password is None"
            return self.get_loginform("", from_page=from_page)
        
        error_msg = check_credentials(username, password)
        if error_msg:
            print "login: if"
            return self.get_loginform(username, error_msg, from_page)
        else:
            print "login: else"
            session = getattr(cherrypy, 'session')
            session[SESSION_KEY] = cherrypy.request.login = username
            setattr(cherrypy, 'session', session)
            cherrypy.request.login = username
            self.on_login(username)
            print "redirecting"
            raise cherrypy.HTTPRedirect(cherrypy.config["app.base_url"])
    
    @cherrypy.expose
    def logout(self):
        sess = getattr(cherrypy, 'session')
        username = sess.get(SESSION_KEY, None)
        sess[SESSION_KEY] = None
        if username:
            cherrypy.request.login = None
            self.on_logout(username)
        raise cherrypy.HTTPRedirect(cherrypy.config["app.base_url"])