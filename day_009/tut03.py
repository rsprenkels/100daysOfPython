import cherrypy
import random
import string

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "static"

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == '__main__':
   cherrypy.server.socket_host = '0.0.0.0' 
   cherrypy.quickstart(StringGenerator(), '/')
