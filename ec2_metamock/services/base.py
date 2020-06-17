import cherrypy

class Service:

    _resources = []

    @cherrypy.expose
    def index(self):
        return "\n".join(self._resources)
