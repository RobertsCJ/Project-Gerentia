import os

def check_module(module) -> bool:
	return True if os.system(f'python -m {module}') == 0  else False
if check_module("pwinput"):
	password_module = 'pwinput'
	from pwinput import pwinput
elif check_module('getpass'):
	password_module = 'getpass'
	from getpass import getpass

