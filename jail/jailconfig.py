from dataclasses import dataclass


@dataclass
class JailConfig:
    pass


@dataclass
class JailConfigDefault:
    enabled: str = 'True of False'
    service_name: str = 'Service name'
    port: str = 'Port'
    filter: str = 'Filter path'
    journalctl : str = 'True or False (if True skip log-path)'
    log_path: str = 'Log path'
    max_retry: str = 'count of retry'
    find_time: str = 'vremya za kotoroe uchitivaetsya ip podozritelnym'
    bantime: str = 'time of ban'
