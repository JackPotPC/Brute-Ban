import configparser
import os


class FilterParser:
    def __init__(self,path):
        self._config = configparser.ConfigParser()
        self._path = path
        self.params = {}

    def _filter_reader(self,filter_name):
        self._config.read(self._path+filter_name)
        if len(self._config.sections()) == 0:
            return 'default'
        return self._config.sections()

    def _config_parser(self, filter_name):
        ffile = self._filter_reader(filter_name)
        if ffile == 'default':
            defaults = self._config.defaults()
            self.params['default'] = defaults
            return self.params
        else:
            for i in ffile:
                self.params.update(self._config.items(i))


    def get_params(self, filter_name):
        self._config_parser(filter_name)
        return self.params



# a = FilterParser()
# print(a.get_params('/filter.conf'))
