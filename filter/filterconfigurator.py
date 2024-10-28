import configparser
import os

from filter.filterconfig import FilterConfig, FilterConfigDefault


#Использовать для добавления через консоль
class FilterConfigurator(FilterConfig):
    def __init__(self):
        super().__init__()
        self._config = configparser.ConfigParser()

    def add_filter(self,filter_name,service_name,regex):
        self._config[f'{filter_name}'] = {'regex':regex}


#Использовать для setup.py
class FilterConfiguratorDefault(FilterConfigDefault):
    def __init__(self):
        super().__init__()
        self._config = configparser.ConfigParser()
        self._config['DEFAULT'] = {'regex':self.regex}

    def set_default_config(self):
        os.mkdir('filters')
        with open ('filters/example.conf', 'w') as file:
            self._config.write(file)


class FilterConfiguratorException(Exception):
    pass


# a = FilterConfiguratorDefault()
# a.set_default_config()
