from src import get_threats
from src.models import Threat
# import sys
# import os
import pytest

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def threats_mock():
    """Setup a test threats list."""
    threats = []
    for _ in range(20):
        threat = Threat('evil', 'evil.com', 'bad', '1/1/2024 00:00 UTC')
        threats.append(threat)
    return threats


@pytest.fixture
def threats_data_mock():
    """Setup a test threats response data."""
    threats = []
    for _ in range(20):
        threat = {'host': 'evil', 'url': 'evil.com',
                  'threat': 'bad', 'date_added': '1/1/2024 00:00 UTC'}
        threats.append(threat)
    return {'urls': threats}


def test_get_threats_data():
    """Test the get_threats_data function with page 2 and a limit of 5."""
    page = 2
    limit = 5
    data = get_threats.get_threats_data(page, limit)
    assert data.get('error') is None
    assert len(data.get('threats')) == limit
    assert data.get('length') is not None


def test_get_threats_data_default():
    """Test the get_threats_data function with no arguments."""
    data = get_threats.get_threats_data()
    assert len(data.get('threats')) == 10
    assert data.get('length') is not None


def test_paginate_threats_data(threats_mock):
    """Test the paginate_threats_data function with page 2 and a limit of 5."""
    page = 2
    limit = 5
    result = get_threats.paginate_threats_data(threats_mock, page, limit)
    assert len(result) == limit


def test_paginate_threats_data_empty():
    """Test the paginate_threats_data function with an empty list."""
    page = 2
    limit = 5
    result = get_threats.paginate_threats_data([], page, limit)
    assert len(result) == 0


def test_extract_urlhaus_data(threats_data_mock):
    """Test the extract_urlhaus_data function."""
    threats = get_threats.extract_urlhaus_data(threats_data_mock)
    assert len(threats_data_mock['urls']) == len(threats)


def test_get_urlhaus_data():
    """Test the get_urlhaus_data function."""
    data = get_threats.get_urlhaus_data()
    assert data.get('error') is None
    assert data.get('urls') is not None
