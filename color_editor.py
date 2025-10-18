from colorama import Fore, Style, init
import os
import keyboard

init(autoreset=True)

all_ability_keys_str = '123456eftrgyq'
movement_keys = ['w', 's', 'd', 'a', 'space']
backspace_str = 'backspace'

def on_key_press(event):
	global all_ability_keys_str, movement_keys, backspace_str

	key = event.name
	clear = lambda: os.system('cls')

	# movment
	if key in movement_keys:
		print(Fore.GREEN + key + Style.RESET_ALL, end=' ', flush=True)

	# ability
	elif key in all_ability_keys_str:
		print(Fore.BLUE + key + Style.RESET_ALL, end='', flush=True)

	# clear
	elif key == backspace_str:
		clear()

	# key does not defined
	else:
		print(Fore.RED + key + Style.RESET_ALL, end='\n', flush=True)

if __name__ == "__main__":
	print(f'''
\'esc\' -> exit
\'backspace\' -> clear

{Fore.BLUE}ABILITIES = {', '.join([key.upper() for key in all_ability_keys_str])}
{Fore.GREEN}MOVMENT & JUMP = {', '.join([key.upper() for key in movement_keys])}
{Fore.RED}NOT defined keys
		''')

	keyboard.on_press(on_key_press)
	keyboard.wait('esc')
