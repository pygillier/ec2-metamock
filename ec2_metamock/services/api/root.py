from bottle import Bottle, run, request
import datetime
import pickle
import base64

api = Bottle()

@api.route('/')
def index():
    """Index endpoint"""
    return "token"

@api.route('/token', method="PUT")
def token():
    """Token endpoint

    See https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
    """
    ttl = request.headers.get('X-aws-ec2-metadata-token-ttl-seconds')
    if ttl is None:
        return
    else:
        try:
            if 1 <= int(ttl) <= 21600:
                now = datetime.datetime.now()
                next = now + datetime.timedelta(seconds=int(ttl))
                payload = {
                    'ttl': ttl,
                    'expires': next.timestamp()
                }
                return base64.b64encode(pickle.dumps(payload))
            else:
                # Invalid value or out-of-bound
                return
        except Exception:
            return ""