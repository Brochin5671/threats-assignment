from dataclasses import dataclass


@dataclass
class Threat:
    host: str
    url: str
    threat_type: str
    date_added: str
