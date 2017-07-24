This is the Biomarkers demo project written in Python using CherryPy.

The 2 key software needed to run the server are - MongoDB and Redis. In addition Cherrypy should be downloaded and installed using pip or otherwise.

The config is specified by the file /application/src/config.py. Definitely check out this file and modify as needed.

To start the server - 
  python web_server.py --env=ENV
  
  where ENV is DEV or PROD
