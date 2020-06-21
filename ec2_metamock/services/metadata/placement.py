import cherrypy

class App:

    _resources = [
        'availability-zone'
    ]

    @cherrypy.expose(alias='availability-zone')
    def availability_zone(self):
        return 'us-east-1'