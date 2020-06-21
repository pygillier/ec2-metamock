import cherrypy
from .. import BaseService
from .defaults import DEFAULTS

@cherrypy.popargs('role_name')
class App(BaseService):

    _resources = [
        'info',
        'security-credentials/'
    ]

    @cherrypy.expose(alias='info')
    def iam_info(self):
        arn = "arn:aws:iam::012345678910:instance-profile/{}".format(DEFAULTS['role_name'])
        return {
            'Code': 'Success',
            'LastUpdated': '2020-06-19T12:59:00Z',
            "InstanceProfileArn" : arn,
            "InstanceProfileId" : "AIP6X577R5YCAZHNBIWRS"
        }

    @cherrypy.expose(alias='security-credentials')
    def security_credentials(self):
        return DEFAULTS['role_name']