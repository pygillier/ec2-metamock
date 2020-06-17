import cherrypy
from .. import BaseService

class App(BaseService):

    _resources = [
        'availability-zone'
    ]

    @cherrypy.expose(alias='availability-zone')
    def availability_zone(self):
        return 'us-east-1'