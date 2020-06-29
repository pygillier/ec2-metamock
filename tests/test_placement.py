import pytest

base_uri = "/latest/meta-data/placement"


@pytest.mark.parametrize(
    "endpoint,content",
    [("", "availability-zone"), ("availability-zone", "us-east-1")],
)
def test_uri(app, endpoint, content):
    uri = "{}/{}".format(base_uri, endpoint)

    resp = app.get(uri)

    assert resp.status_code == 200
    assert content in resp
