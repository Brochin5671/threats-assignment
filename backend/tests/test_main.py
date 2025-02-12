from main import app
# import sys
# import os
import pytest

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def client():
    """Setup a test client for the app."""
    with app.test_client() as client:
        yield client


def test_threats(client):
    """Test the /api/threats/ endpoint with page 2 and limit of 5."""
    page = 2
    limit = 5
    res = client.get(f'/api/threats?page={page}&limit={limit}')
    assert res.status_code == 200
    data = res.json
    assert len(data.get('threats')) == limit


def test_threats_default(client):
    """Test the /api/threats/ endpoint with no params. Should default to page 1 and a limit of 10."""
    res = client.get('/api/threats')
    assert res.status_code == 200
    data = res.json
    assert len(data.get('threats')) == 10


def test_threats_missing_limit(client):
    """Test the /api/threats/ endpoint without the limit param."""
    page = 1
    res = client.get(f'/api/threats?page={page}')
    assert res.status_code == 400
    data = res.json
    assert data.get('error') is not None


def test_threats_missing_page(client):
    """Test the /api/threats/ endpoint without the page param."""
    limit = 5
    res = client.get(f'/api/threats?limit={limit}')
    assert res.status_code == 400
    data = res.json
    assert data.get('error') is not None
