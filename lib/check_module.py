import os

def check_module(module) -> bool:
	if os.system(f'python -m {module}') == 0:
		return True
	else:
		return False
if check_module("pwinput"):
	password_module = 'pwinput'
	from pwinput import pwinput
elif check_module('getpass'):
	password_module = 'getpass'
	from getpass import getpass

