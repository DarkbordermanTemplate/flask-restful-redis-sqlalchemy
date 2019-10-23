import os
import json
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app(os.environ.get('APP_SETTINGS', 'testing'))
    with app.app_context():
        yield app.test_client()


ROOT_OUTPUT = {
    'success': {
        'status': 200,
        'body': 'hello world'
    }
}
ROOT_URL = 'http://localhost:5000/'
ROOT_TEST_TYPE = ['success']


@pytest.mark.parametrize('test_type', ROOT_TEST_TYPE)
def test_root(client, test_type):
    resp = client.get(ROOT_URL)
    assert resp.status_code == ROOT_OUTPUT[test_type]['status']
    resp = json.loads(resp.data.decode())
    body = ROOT_OUTPUT[test_type]['body']
    assert resp == body
