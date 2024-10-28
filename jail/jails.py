import os

from filter.filterparser import FilterParser
from jail.jailparser import JailParser
from action.actionparser import ActionParser

class Jails:
    def __init__(self,path='/home/jackpot/projects/BruteBan/'):
        self._jailparser = JailParser(path)
        self._filterparser = FilterParser(path)
        self._actionparser = ActionParser(path)
        self._jails_options = {}
        self._active_instructions = {}

    def _read_jails_options(self):
        self._jails_options = self._jailparser.get_params()

    def _get_filter_options(self, name):
        fopt = self._filterparser.get_regex(name)
        return fopt

    def _get_action_options(self, name):
        aopt = self._actionparser.get_action(name)
        return aopt

    #Получает все активные инструкции
    def _config_coordination(self):
        self._read_jails_options()
        for i in self._jails_options:
            if self._jails_options[i]['enabled'] == 'True':
                filter = self._get_filter_options(self._jails_options[i]['filter'])
                action = self._get_action_options(self._jails_options[i]['action'])
                if filter and action:
                    self._active_instructions[i] = self._jails_options[i]
                    self._active_instructions[i]['filter'] = filter
                    self._active_instructions[i]['action'] = action

    def get_options(self):
        self._config_coordination()
        return self._active_instructions


# a = Jails()
# print(a.get_option())
