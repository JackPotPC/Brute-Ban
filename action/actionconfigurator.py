import configparser
import os

from action.actionconfig import ActionConfig, ActionConfigDefault


class ActionConfigurator:
    pass


class ActionConfiguratorDefault(ActionConfigDefault):
    def __init__(self):
        super().__init__()
        self._config = configparser.ConfigParser()
        self._config['DEFAULT'] = {'command': self.command}

    def set_default_config(self):
        os.mkdir('actions')
        with open('example.conf', 'w') as file:
            self._config.write(file)


class ActionConfiguratorException(Exception):
    pass


# a = ActionConfiguratorDefault()
# a.set_default_config()
