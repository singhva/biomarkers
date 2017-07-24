'''
Created on Sep 8, 2014

@author: varun
'''
import threading
import urllib2

def my_service():
    print "My name is: "+str(threading.current_thread())
    resp = urllib2.urlopen("http://www.google.com")
    print resp.getcode()

def main():
    print "starting...."
    print threading.current_thread()
    t = threading.Thread(name='url_thread', target=my_service)
    t.start()
    print "ending"

if __name__ == '__main__':
    main()