import cherrypy
from . import services
from .services import metadata, api

def run():
    cherrypy.tree.mount(metadata.Root(), '/latest/meta-data/')
    cherrypy.tree.mount(metadata.Placement(), '/latest/meta-data/placement/')
    
    cherrypy.tree.mount(api.Root(), '/latest/api/')
    cherrypy.engine.start()
    cherrypy.engine.block()
