from bottle import Bottle, run, request

services = Bottle()

_resources = [
        'domain',
        'partition'
    ]

@services.route('/')
def index():
    return "\n".join(_resources)


@services.route('/domain')
def domain():
    return 'amazonaws.com'

@services.route('/partition')
def partition():
    return 'aws'
