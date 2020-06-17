import cherrypy

from .. import BaseService

class App(BaseService):

    _resources = [
        'domain',
        'partition'
    ]

    @cherrypy.expose(alias='domain')
    def domain(self):
        return 'amazonaws.com'

    @cherrypy.expose(alias='partition')
    def partition(self):
        return 'aws'
