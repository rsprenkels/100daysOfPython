import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "changed"

if __name__ == '__main__':
   cherrypy.server.socket_host = '0.0.0.0' 
   cherrypy.quickstart(Root(), '/')
