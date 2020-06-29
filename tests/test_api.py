import pytest
base_uri = '/latest/api'


def test_index(app):
    resp = app.get(base_uri)

    assert resp.status_code == 200
    assert 'token' in resp


@pytest.mark.parametrize('ttl', [
    '10',
    '21601',
    'aaa',
])
def test_token(app, ttl):
    # TODO check response content & decode it
    uri = "{}/token".format(base_uri)

    assert app.get(uri, expect_errors=True).status == "405 Method Not Allowed"


    resp = app.put(uri, headers=[
        ('X-aws-ec2-metadata-token-ttl-seconds', ttl)
    ])

    assert resp.status_code == 200
