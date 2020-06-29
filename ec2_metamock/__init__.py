from bottle import Bottle
from .services import metadata, api


app = Bottle()

app.mount("/latest/api", api.api)
app.mount("/latest/meta-data/services", metadata.services)
app.mount("/latest/meta-data/placement", metadata.placement)
app.mount("/latest/meta-data", metadata.root)
