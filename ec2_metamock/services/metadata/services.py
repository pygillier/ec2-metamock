import cherrypy

from .. import BaseService

class App(BaseService):

    _resources = [
        'domain',
        'partition'
    ]

    @cherrypy.expose(alias='domain')
    def availability_zone(self):
        return 'amazonaws.com'

    @cherrypy.expose(alias='partition')
    def availability_zone(self):
        return 'aws'
