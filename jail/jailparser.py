import configparser

class JailParser:
    def __init__(self,path):
        self._config = configparser.ConfigParser()
        self._path = path
        self.params = {}

    #изменить добавив путь
    def _jail_reader(self):
        self._config.read(self._path + '/jail/jail.conf')
        if len(self._config.sections()) == 0:
            return 'default'
        return self._config.sections()

    def _config_parser(self):
        ffile = self._jail_reader()
        if ffile == 'default':
            defaults = self._config.defaults()
            self.params['default'] = defaults
            return self.params
        else:
            for i in ffile:
                temp_dict = {}
                for j in self._config.items(i):
                    temp_dict.update({j[0]: j[1]})
                self.params[i] = temp_dict

    def get_params(self):
        self._config_parser()
        return self.params

# a = JailParser()
# print(a.get_params())