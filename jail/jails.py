import os

from filter.filterparser import FilterParser
from jail.jailparser import JailParser
from action.actionparser import ActionParser

class Jails:
    def __init__(self,path='/home/jackpot/projects/BruteBan/'):
        self._path = path
        self._jailparser = JailParser(self._path)
        self._filterparser = FilterParser(self._path)
        self._actionparser = ActionParser()
        self._jailparams = {}
        self._filterparams = {}
        self._actionparams = {}
        self._active_instructions = {}

    def _set_jailparams(self):
        self._jailparams = self._jailparser.get_params()

    def _get_filterparams(self, name):
        self._filterparams = self._filterparser.get_params('filter/' + name)
        return self._filterparams

    def _get_jailparams(self):
        self._set_jailparams()
        return self._jailparams

    def _config_coordination(self):
        self._set_jailparams()
        for i in self._jailparams:
            if self._jailparams[i]['enabled'] == 'True':
                filter = self._get_filterparams(self._jailparams[i]['filter'])
                if filter:
                    self._active_instructions[i] = self._jailparams[i]
                    self._active_instructions[i]['filter'] = filter

    def get_option(self):
        self._config_coordination()
        return self._active_instructions


# a = Jails()
# print(a.get_instruction())