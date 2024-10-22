import re
import socket
import os
import asyncio
import subprocess

from jail.jails import Jails

class BruteBan:
    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._path = os.getcwd()
        self._jails = Jails(self._path).get_option()

    #После добавления измненения команды journcalctl изменить этот метод
    def journalctl_option(self,instruction):
        return instruction['journalctl'] == 'True' and instruction['log_path'] == 'False'

    async def get_logs(self,jail_name):
        if self.journalctl_option(self._jails[jail_name]):
            process = await asyncio.create_subprocess_exec('journalctl', '-f' '-u', 'sshd.service',
                                                           stdout=asyncio.subprocess.PIPE,
                                                           stderr=asyncio.subprocess.PIPE)
            print(f'{process}')
            return process

    async def process_log(self, jail_name):
        while True:
            process = await self.get_logs(jail_name)
            if not process:
                return

            pattern = re.compile(
                r'Failed password for (invalid user \w+|\w+) from (\d+.\d+.\d+.\d+) port (\d+)'
            )
            unique_ips = set()

            try:
                while True:
                    line = await process.stdout.readline()

                    if not line and process.returncode is not None:
                        # Если процесс завершился, перезапускаем отслеживание логов
                        print(f"Служба {jail_name} завершила работу, перезапуск отслеживания...")
                        break  # Выходим из внутреннего цикла и перезапускаем процесс

                    if line:
                        logs = line.decode('utf-8')
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
                                    print(f"IP заблокирован: {ip_address} для сервиса {jail_name}")
            except asyncio.CancelledError:
                process.terminate()  # Завершаем процесс при прерывании
                break

    async def log_tracking(self):
        tasks = [self.process_log(jail_name) for jail_name in self._jails]
        await asyncio.gather(*tasks)


def run():
    brute_ban = BruteBan()
    asyncio.run(brute_ban.log_tracking())

run()