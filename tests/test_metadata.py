import pytest

base_uri = "/latest/meta-data"


@pytest.mark.parametrize(
    "endpoint,content",
    [("", "ami-id"), ("", "profile"), ("instance-id", "i-0235ba33af8e86af4")],
)
def test_uri(app, endpoint, content):
    uri = "{}/{}".format(base_uri, endpoint)

    resp = app.get(uri)

    assert resp.status_code == 200
    assert content in resp


def test_ipv4_404(app):

    uri = "{}/public-ipv4".format(base_uri)

    assert app.get(uri, expect_errors=True).status_code == 404
