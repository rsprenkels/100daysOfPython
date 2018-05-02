import cherrypy
import random
import string

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "static"

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))

if __name__ == '__main__':
   cherrypy.server.socket_host = '0.0.0.0' 
   cherrypy.quickstart(StringGenerator(), '/')
