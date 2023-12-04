import os

def check_module(module) -> bool:
	return True if os.system(f'python3 -m {module}') == 0  else False


if check_module("pwinput"):
	from pwinput import pwinput
	password_module = lambda input: pwinput(input)

elif check_module('getpass'):
	from getpass import getpass
	password_module = lambda input: getpass(input)
