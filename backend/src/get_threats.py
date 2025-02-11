import requests
from .models import Threat


def get_urlhaus_data(limit: int | None):
    url = 'https://urlhaus-api.abuse.ch/v1/urls/recent/'
    if limit:
        url += f'limit/{limit}/'

    data = None
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.RequestException as e:
        data = None
    return data


def extract_urlhaus_data(data):
    # TODO: check data['urls']
    threats = []
    for item in data['urls']:
        threat = Threat(item['host'], item['url'],
                        item['threat'], item['date_added'])
        threats.append(threat)
    return threats


def get_threats_data(limit: int | None = None) -> list[Threat]:
    data = get_urlhaus_data(limit)
    threats = extract_urlhaus_data(data)
    return threats
