import configparser

from jails.jailconfig import JailConfig,JailConfigDefault

class JailConfigurator:
    pass


class JailConfiguratorDefault(JailConfigDefault):
    def __init__(self):
        super().__init__()
        self._config = configparser.ConfigParser()
        self._config['DEFAULT'] = {'enabled': self.enabled,
                                   'service_name': self.service_name,
                                   'port': self.port,
                                   'filter': self.filter,
                                   'journalctl': self.journalctl,
                                   'log_path': self.log_path,
                                   'max_retry': self.max_retry,
                                   'find_time': self.find_time,
                                   'bantime': self.bantime}

    def set_default_config(self):
        with open ('jail.conf', 'w') as file:
            self._config.write(file)


class JailConfiguratorException(Exception):
    pass

# a = JailConfiguratorDefault()
# a.set_default_config()