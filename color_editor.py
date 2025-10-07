from colorama import Fore, Style, init
import os

init(autoreset=True)

import keyboard


def on_key_press(event):

	key = event.name
	clear = lambda: os.system('cls')

	# movment
	if key in ['w', 's', 'd', 'a', 'space']:
		print(Fore.GREEN + key + Style.RESET_ALL, end=' ', flush=True)

	# ability
	elif key in '1234eftrgyq5':
		print(Fore.BLUE + key + Style.RESET_ALL, end='', flush=True)

	# clear
	elif key == 'backspace':
		clear()

	# key does not defined
	else:
		print(Fore.RED + key + Style.RESET_ALL, end='\n', flush=True)

print("start!\n'esc' to exit\n")
keyboard.on_press(on_key_press)
keyboard.wait('esc')
