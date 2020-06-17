import cherrypy

from .. import BaseService

class App(BaseService):

    _resources = [
        'domain',
        'partition'
    ]

    @cherrypy.expose(alias='availability-zone')
    def availability_zone(self):
        return 'us-east-1'