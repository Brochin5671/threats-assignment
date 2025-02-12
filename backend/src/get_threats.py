import requests
from .models import Threat


def get_urlhaus_data(limit: int | None = None):
    url = 'https://urlhaus-api.abuse.ch/v1/urls/recent/'
    # Get threats using a limit if provided
    if limit:
        url += f'limit/{limit}/'

    # Call urlhaus-api and return data as a JSON
    data = {}
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException as e:
        data['error'] = str(e)  # TODO: handle err message
    return data


def extract_urlhaus_data(data) -> list[Threat]:
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


def paginate_threats_data(threats: list, page: int, limit: int) -> list[Threat]:
    start = (page - 1) * limit
    end = start + limit
    return threats[start:end]


def get_threats_data(page: int = 1, limit: int = 10):
    # Get data from API
    data = get_urlhaus_data()
    if data.get('error'):
        return data

    # Extract and return data from JSON
    threats = extract_urlhaus_data(data)
    return {'threats': paginate_threats_data(threats, page, limit)}
