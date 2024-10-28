from dataclasses import dataclass


@dataclass
class JailConfig:
    pass


@dataclass
class JailConfigDefault:
    service_name: str = 'Service Name'
    enabled: str = 'True of False'
    port: str = 'Port'
    filter: str = 'Filter path'
    log_path: str = 'Log path or name of systemd'
    ignore_ip: str = 'list of ignoring ip_adresses'
    max_retry: str = 'count of retry'
    find_time: str = 'vremya za kotoroe uchitivaetsya ip podozritelnym'
    action: str = 'action path'
    bantime: str = 'time of ban'
