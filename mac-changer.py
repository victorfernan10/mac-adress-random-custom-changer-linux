#!/usr/bin/env python

import string
import subprocess
import random
from colorama import Fore

tamanho = 2
escolha = str(input('\n[1] - Random MAC\n[2] - Custom MAC\n\n' + Fore.BLUE + "[1] - [2]: "))

if escolha == '1':
    bla = "".join(random.choices(string.digits, k=tamanho))
    random_mac = (bla + ":" + bla + ":" + bla + ":" + bla + ":" + bla + ":" + bla)
    subprocess.call("sudo ifconfig eth0 down", shell=True)
    subprocess.call("sudo ifconfig eth0 hw ether " + random_mac, shell=True)
    subprocess.call('sudo ifconfig eth0 up', shell=True)
    print("MAC trocado para ",Fore.RED + random_mac)
else:
    custom_mac = str(input('Qual sera o novo MAC? '))
    subprocess.call("sudo ifconfig eth0 down", shell=True)
    subprocess.call("sudo ifconfig eth0 hw ether " + custom_mac, shell=True)
    subprocess.call("sudo ifconfig eth0 up", shell=True)
    print("MAC trocado para ",Fore.RED + custom_mac)


