import pytest

base_uri = "/latest/meta-data/placement"


@pytest.mark.parametrize(
    "endpoint,content",
    [("", "availability-zone"), ("availability-zone", "us-east-1"),],  # noqa
)
def test_uri(app, endpoint, content):
    # TODO check response content & decode it
    uri = "{}/{}".format(base_uri, endpoint)

    resp = app.get(uri)

    assert resp.status_code == 200
    assert content in resp
