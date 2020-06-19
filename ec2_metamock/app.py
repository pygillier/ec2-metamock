import cherrypy
from . import services
from .services import metadata, api

def run():
    cherrypy.tree.mount(metadata.Root(), '/latest/meta-data/')
    cherrypy.tree.mount(metadata.Placement(), '/latest/meta-data/placement/')
    cherrypy.tree.mount(metadata.Services(), '/latest/meta-data/services/')
    cherrypy.tree.mount(metadata.Iam(), '/latest/meta-data/iam/')
    
    cherrypy.tree.mount(api.Root(), '/latest/api/')
    cherrypy.engine.start()
    cherrypy.engine.block()
