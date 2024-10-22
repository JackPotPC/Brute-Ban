import configparser

from filter.filterconfig import FilterConfig, FilterConfigDefault


#Использовать для добавления через консоль
class FilterConfigurator(FilterConfig):
    def __init__(self):
        super().__init__()
        self._config = configparser.ConfigParser()

    def add_filter(self,filter_name,service_name,regex):
        self._config[f'{filter_name}'] = {'filter_name':filter_name,
                                          'service_name':service_name,
                                          'regex':regex}



#Использовать для setup.py
class FilterConfiguratorDefault(FilterConfigDefault):
    def __init__(self):
        super().__init__()
        self._config = configparser.ConfigParser()
        self._config['DEFAULT'] = {'filter_name':self.filter_name,
                                   'service_name':self.service_name,
                                   'regex':self.regex}

    def set_default_config(self):
        with open ('filter.conf', 'w') as file:
            self._config.write(file)


class FilterConfiguratorException(Exception):
    pass


# a = FilterConfiguratorDefault()
# a.set_default_config()
