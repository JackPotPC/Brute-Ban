import configparser

class ActionParser:
    def __init__(self):
        self._config = configparser.ConfigParser()
        # self.path = path
        self.params = {}

    def get_params(self):
        # self._config_parser()
        return self.params