from bottle import Bottle, route
from .services import metadata, api


app = Bottle()

app.mount('/latest/api', api.service)


def run():
    app.run(host='localhost', port=8080, debug=True)
