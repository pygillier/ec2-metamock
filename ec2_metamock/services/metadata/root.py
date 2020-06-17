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

    @cherrypy.expose(['hostname', 'local-hostname'])
    def local_hostname(self):
        return "ip-10.11.12.13.us-east-1.compute.internal"

    @cherrypy.expose(alias='instance-action')
    def ami_instance_action(self):
        return "none"

    @cherrypy.expose(alias='instance-id')
    def instance_id(self):
        return "i-0235ba33af8e86af4"

    @cherrypy.expose(alias='instance-type')
    def instance_type(self):
        return "t3.small"

    @cherrypy.expose(alias='local-ipv4')
    def local_ipv4(self):
        return "10.11.12.13"

    @cherrypy.expose
    def mac(self):
        return "e9:8b:53:68:9a:20"

    @cherrypy.expose
    def profile(self):
        return 0

    @cherrypy.expose(alias='reservation-id')
    def reservation_id(self):
        return "r-01c15d13beef4376d"

    @cherrypy.expose(alias='security-groups')
    def security_groups(self):
        return "\n".join([
            'security-group-one',
            'security-group-two',
            'security-group-three',
        ])
