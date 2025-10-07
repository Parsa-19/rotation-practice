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

if __name__ == "__main__":
	print(f"""'esc' -> exit
{Fore.BLUE}ABILITY = 1, 2, 3, 4, e, f, t, r, g, y, q, 5
{Fore.GREEN}MOVMENT & JUMP = W, A, S, D, 'space'
{Fore.RED}NOT defined keys
		""")

	keyboard.on_press(on_key_press)
	keyboard.wait('esc')
