import pytest
from webtest import TestApp
from ec2_metamock import app as App

@pytest.fixture(scope="module")
def app():
    test_app = TestApp(App.app)
    return test_app