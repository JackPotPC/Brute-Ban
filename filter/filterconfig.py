from dataclasses import dataclass


@dataclass
class FilterConfig:
    regex: str


@dataclass
class FilterConfigDefault:
    regex: str = 'Regex'
