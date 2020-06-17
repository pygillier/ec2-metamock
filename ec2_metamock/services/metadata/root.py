import cherrypy
from .. import BaseService

class App(BaseService):

    _resources = [
        'ami-id',
        'ami-launch-index',
        'ami-manifest-path',
        'block-device-mapping/',
        'events/',
        'hostname',
        'iam/',
        'instance-action',
        'instance-id',
        'instance-type',
        'local-hostname',
        'local-ipv4',
        'mac',
        'metrics/',
        'network/',
        'placement/',
        'profile',
        'public-hostname',
        'public-ipv4',
        'public-keys/',
        'reservation-id',
        'security-groups',
        'services/',
    ]

    @cherrypy.expose(alias='ami-id')
    def ami_id(self):
        return "ami-0abcdef1234567890"

    @cherrypy.expose(alias='ami-launch-index')
    def ami_launch_index(self):
        return 0

    @cherrypy.expose(alias='ami-manifest-path')
    def ami_manifest_path(self):
        return "(unknown)"

    @cherrypy.expose(alias='hostname')
    def ami__local_hostname(self):
        return "ip-10.11.12.13.us-east-1.compute.internal"

    @cherrypy.expose(alias='instance-action')
    def ami_instance_action(self):
        return "none"

    # @cherrypy.expose(alias='instance-id')
    def ami_launch_index(self):
        return 0

    # @cherrypy.expose(alias='instance-type')
    def ami_launch_index(self):
        return 0

    # @cherrypy.expose(alias='local-hostname')
    def ami_launch_index(self):
        return 0

    # @cherrypy.expose(alias='local-ipv4')
    def ami_launch_index(self):
        return 0

    # @cherrypy.expose(alias='mac')
    def ami_launch_index(self):
        return 0

    # @cherrypy.expose(alias='profile')
    def ami_launch_index(self):
        return 0

    @cherrypy.expose(alias='reservation-id')
    def ami_launch_index(self):
        return "r-01c15d1c4375ace6d"

    # @cherrypy.expose(alias='security-groups')
    def ami_launch_index(self):
        return 0
