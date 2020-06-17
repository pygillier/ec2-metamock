import cherrypy
from cherrypy.test import helper

from ec2_metamock.services.metadata import Services

class ServicesTest(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(Services(), '/', {})

    def test_index(self):
        self.getPage("/")
        self.assertStatus('200 OK')

    def test_domain(self):
        self.getPage("/domain")
        self.assertStatus('200 OK')

    def test_partition(self):
        self.getPage("/partition")
        self.assertStatus('200 OK')
