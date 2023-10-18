from time import sleep
from colorama import Fore

def run(typeEffect, clear):
  clear()
  typeEffect.fast(Fore.GREEN+"Hello! "+Fore.WHITE+"Before we get started, let's get some basic controls down. To select through menus, use wasd, depending on which way the menu moves. To select an option, hit enter."+Fore.YELLOW+" To begin, hit the enter key. Have fun!"+Fore.WHITE)
  input()
  return True