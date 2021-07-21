from termcolor import colored
from inspect import getsourcefile
from os.path import abspath

def is_error(log):
    status = colored('ERROR', 'red')
    path = abspath(getsourcefile(lambda: 0))
    print(f'[{status}]: {log}')
    open('logs.log', 'a').write(f'[ERROR] {path} ({log})\n')


def is_complied(log):
    status = colored('OK', 'green')
    path = abspath(getsourcefile(lambda: 0))
    print(f'[ {status} ]: {log}')


def clean_log():
    open('logs.log', 'w').write('')