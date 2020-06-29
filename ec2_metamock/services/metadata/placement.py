from bottle import Bottle

placement = Bottle()

_resources = ["availability-zone"]


@placement.route("/")
def index():
    return "\n".join(_resources)


@placement.route("/availability-zone")
def domain():
    return "us-east-1"
