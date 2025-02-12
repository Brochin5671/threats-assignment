import requests
from .models import Threat


def get_urlhaus_data():
    """Calls the urlhaus-api and tries to return the response as a JSON."""
    url = 'https://urlhaus-api.abuse.ch/v1/urls/recent/'

    # Call urlhaus-api and return data as a JSON
    data = {}
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException as e:
        data['error'] = 'Something went wrong on our end.'
        print(e)
    return data


def extract_urlhaus_data(data) -> list[Threat]:
    """Extracts required threat data from the JSON to return as a list."""
    # Extract just the host, url, threat type, and date added attributes from each object in JSON
    threats = []
    for item in data['urls']:
        threat = Threat(item['host'],
                        item['url'],
                        item['threat'],
                        item['date_added'])
        threats.append(threat)
    # Return extracted data as a list of objects
    return threats


def paginate_threats_data(threats: list[Threat], page: int, limit: int) -> list[Threat]:
    """Returns a chunk of the threats list for pagination."""
    start = (page - 1) * limit
    end = start + limit
    return threats[start:end]


def get_threats_data(page: int = 1, limit: int = 10):
    """Tries to return the threat data for the /api/threats/ endpoint."""
    # Get data from API
    data = get_urlhaus_data()
    if data.get('error'):
        return data

    # Extract and return data from JSON
    threats = extract_urlhaus_data(data)
    return {'threats': paginate_threats_data(threats, page, limit), 'length': len(threats)}
