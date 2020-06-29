import pytest

base_uri = '/latest/meta-data/services'


@pytest.mark.parametrize('endpoint,content', [
    ('', 'domain'),
    ('domain', 'amazonaws.com'),
    ('partition', 'aws'),
])
def test_uri(app, endpoint, content):
    # TODO check response content & decode it
    uri = "{}/{}".format(base_uri, endpoint)

    resp = app.get(uri)


    assert resp.status_code == 200
    assert content in resp