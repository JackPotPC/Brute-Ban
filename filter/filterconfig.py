from dataclasses import dataclass


@dataclass
class FilterConfig:
    filter_name: str
    service_name: str
    regex: str


@dataclass
class FilterConfigDefault:
    filter_name: str = 'Name'
    service_name: str = 'Service name'
    regex: str = 'Regex'