import socket
import os
import subprocess
import re
from jail.jails import Jails
matchess = {'SSHD': 'sshd.service'}
class BruteBan:
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._path = os.getcwd() + '/'
        #Получает все активные инструкции
        self._jails = Jails(self._path).get_options()

    #После добавления измненения команды journcalctl изменить этот метод
    def journalctl_option(self,instruction):
        return instruction['log_path'] == 'journalctl'

    def search_for_matches(self,name):
        if name in matchess:
            return matchess.get(name)

    def get_logs(self,name):
        sname = self.search_for_matches(name)
        print(self._jails)
        print(sname)
        if self.journalctl_option(self._jails[f'{name}']):
            result = subprocess.run(['journalctl', '-f', '-u', f'{sname}'], capture_output=True,                                text=True)
            return result.stdout

    def log_tracking(self):
        for i in self._jails:
            process = self.get_logs(i)
            pattern = re.compile(
                rf'{self._jails[i]["filter"][0][1]}'
            )
            unique_ips = set()
            try:
                while True:
                    output = process.stdout.readline()
                    if output == b'' and process.poll() is not None:
                        break
                    if output:
                        logs = output.decode('utf-8')
                        matches = pattern.findall(logs)
                        # Обработка совпадений
                        for match in matches:
                            if match[0]:  # Если это неуспешная попытка входа
                                user = match[0]
                                ip_address = match[1]
                                port = match[2]
                                if ip_address not in unique_ips:
                                    unique_ips.add(ip_address)
                                    subprocess.run(['iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'],
                                                   capture_output=True)
                                    print(match[1])
            except KeyboardInterrupt:
                process.terminate() 


def run():
    a = BruteBan()
    print("nvim is working")
    while True:
        a.log_tracking()



run()
# a = BruteBan()
# print(a._get_filterparams())
# print(a.get_jailparams())
# print(a.config_coordination())
# a.log_option() 
