from bottle import Bottle, abort
from .services import services
from .placement import placement

root = Bottle()

_resources = [
    "ami-id",
    "ami-launch-index",
    "ami-manifest-path",
    "block-device-mapping/",  # Not implemented yet
    "events/",  # Not implemented yet
    "hostname",
    "iam/",  # Not implemented yet
    "instance-action",
    "instance-id",
    "instance-type",
    "local-hostname",
    "local-ipv4",
    "mac",
    "metrics/",  # Not implemented yet
    "network/",  # Not implemented yet
    "placement/",
    "profile",
    "public-hostname",
    "public-ipv4",
    "public-keys/",  # Not implemented yet
    "reservation-id",
    "security-groups",
    "services/",
]


@root.route("/")
def index():
    return "\n".join(_resources)


@root.route("/ami-id")
def ami_id():
    return "ami-0abcdef1234567890"


@root.route("/ami-launch-index")
def ami_launch_index():
    return 0


@root.route("/ami-manifest-path")
def ami_manifest_path():
    return "(unknown)"


@root.route("/hostname")
@root.route("/local-hostname")
def local_hostname():
    return "ip-10.11.12.13.us-east-1.compute.internal"


@root.route("/instance-action")
def ami_instance_action():
    return "none"


@root.route("/instance-id")
def instance_id():
    return "i-0235ba33af8e86af4"


@root.route("/instance-type")
def instance_type():
    return "t3.small"


@root.route("/local-ipv4")
def local_ipv4():
    return "10.11.12.13"


@root.route("/mac")
def mac():
    return "e9:8b:53:68:9a:20"


@root.route("/profile")
def profile():
    return "default-hvm"


@root.route("/public-ipv4")
def public_ipv4():
    abort(404, "")


@root.route("/reservation-id")
def reservation_id():
    return "r-01c15d13beef4376d"


@root.route("/security-groups")
def security_groups():
    return "\n".join(
        ["security-group-one", "security-group-two", "security-group-three"]
    )
