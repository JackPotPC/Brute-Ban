from dataclasses import dataclass


@dataclass
class ActionConfig:
    pass


@dataclass
class ActionConfigDefault:
    command: str = 'Command'

