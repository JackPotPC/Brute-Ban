import configparser
import os


class FilterParser:
    def __init__(self,path='/home/jackpot/projects/BruteBan'):
        self._config = configparser.ConfigParser()
        self._path = path
        self.regex = {}

    def _filter_reader(self, name):
        self._config.read(self._path + f'/filter/filters/{name}')
        return self._config.items(''.join(self._config.sections()))

    def _config_parser(self, filter_name):
        self.regex = self._filter_reader(filter_name)


    def get_regex(self, name):
        self._config_parser(name)
        return self.regex



# a = FilterParser()
# print(a.get_regex('ssh.conf'))
