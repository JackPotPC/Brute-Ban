import configparser


class ActionParser:
    def __init__(self,path='/home/jackpot/projects/BruteBan'):
        self._config = configparser.ConfigParser()
        self._path = path
        self.command = {}

    def _action_reader(self, name):
        self._config.read(self._path + f'/action/actions/{name}')
        return self._config.items(''.join(self._config.sections()))

    def _action_parser(self, name):
        self.command = self._action_reader(name)[0][1]

    def get_action(self, name):
        self._action_parser(name)
        return self.command

# a = ActionParser()
# print(a.get_params(name='email.conf'))
