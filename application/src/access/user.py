'''
Created on May 27, 2014

@author: varun
'''
from datetime import datetime
import getpass
import md5
import pprint

from config import get_db_connection


class User(object):
    '''
    classdocs
    '''
    GROUPS = ["USER", "ADMIN"]

    def __init__(self, username=None, password=None, groups = None, last_updated = None):
        '''
        Constructor
        '''
        if username:
            self.username = username
        if password:
            self.password = password
        self.groups = groups or ["USER"]
        self.last_updated = last_updated or datetime.utcnow()
        
    @staticmethod
    def get_by_username(username):
        db = get_db_connection()
        result = db["USERS"].find_one({"username": username})
        if result:
            user = User(username=result["username"], password=result["password"], groups=result["groups"], last_updated=result["last_updated"])
            return user
        
    def save(self):
        db = get_db_connection()
        user = {"username":self.username, "password":md5.new(self.password).hexdigest(), "groups":self.groups, "last_updated":self.last_updated}
        pprint.pprint(user)
        db["USERS"].save(user)
        
def interactive():
    print "Inside interactive user creation"
    user = User()
    username = password = confirm = ""
    while username.strip() == "":
        username = raw_input("Enter username: ")
    
    user.username = username
    
    while password.strip() == "":
        password = getpass.getpass("Enter password: ")
        password.strip()
        if password != "":
            while confirm == "":
                confirm = getpass.getpass("Enter password again (type END to re-enter password): ")
                confirm = confirm.strip()
                if confirm == "END": 
                    password = confirm = ""
                    break
                elif confirm != "" and confirm != password:
                    print "Passwords don't match. Try again."
                    confirm = ""
        
    user.password = password
    
    groups = raw_input("Enter comma separated groups (USER, ADMIN) [default USER]: ")
    if groups.strip() != "":
        temp = [group for group in groups.strip().split(",") if group in User.GROUPS]
        if len(temp) > 0: user.groups = temp
        
    return user
    
    
if __name__ == '__main__':
    user = interactive()
    user.save()