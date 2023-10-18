from colorama import Fore
import sys
import json
from time import sleep

def run(typeEffect, clear):
  clear()
  with open('./data/player.json', 'w') as f: f.write('')
  with open('./data/stagesComplete.json', 'w') as f: f.write("{\"stagesCompleted\":0}")
  info = {}
  info["health"] = 100
  typeEffect.medium('Welcome to the Lost Kingdom!\n')
  typeEffect.medium('You are a brave adventurer seeking treasure.\n')
  typeEffect.medium("But before we get to all that, we must get you started off.")
  typeEffect.medium(Fore.YELLOW+"What is your name?"+Fore.WHITE)
  info["name"] = input("|>")
  typeEffect.medium("\nWell, "+info["name"]+", there are 4 classes to get you started: ")
  typeEffect.medium(Fore.RED+"  -The Fighter, who wields swords and other various long melee weapons. Cannot use ranged weapons or magic attacks")
  typeEffect.medium(Fore.GREEN+"  -The Archer, who wields bows and other ranged weapons, but cannot use melee or magic attacks.")
  typeEffect.medium(Fore.LIGHTBLACK_EX+"  -The Assassin, who wields short melee weapons and some stealth related magic attacks.")
  typeEffect.medium(Fore.BLUE+"  -The Mage, who wields magical weapons and excels at magic attacks, however cannot use melee or ranged weapons.")
  typeEffect.medium(Fore.YELLOW+"\nWhich one would you like? Fighter, Archer, Assassin, or Mage?"+Fore.WHITE)
  repeats = 0
  while True:
    clas = input("|>")
    if clas.lower() == "fighter": info["class"] = "fighter"; break
    elif clas.lower() == "archer": info["class"] = "archer"; break
    elif clas.lower() == "assassin": info["class"] = "assassin"; break
    elif clas.lower() == "mage": info["class"] = "mage"; break
    else: 
      if repeats == 0: typeEffect.fast(Fore.RED+"That's not how to spell that! Try Again!"+Fore.WHITE); repeats += 1
      elif repeats == 1: typeEffect.fast(Fore.RED+"Are you serious? Just copy and paste it at this point. Again!"+Fore.WHITE); repeats += 1
      elif repeats == 2: typeEffect.fast(Fore.RED+"At this point, you don't deserve to have a class. Again!"+Fore.WHITE); repeats += 1
      elif repeats == 3: typeEffect.fast(Fore.RED+"You have to be joking at this point.. Again!"+Fore.WHITE); repeats += 1
      elif repeats == 4: typeEffect.fast(Fore.RED+"If you mess it up again you're gonna have to restart the game.. Again!"+Fore.WHITE); repeats += 1
      elif repeats == 5: typeEffect.fast(Fore.RED+"You asked for it.. Bye!"+Fore.WHITE); sys.exit()

  if info["class"] == "fighter":
    info["inventory"] = {"weapons":['./weapons/swords/basicsword.json'], "items":['./items/potions/healthpotion.json', './items/potions/healthpotion.json']}
  elif info["class"] == "archer":
    info["inventory"] = {"weapons":['./weapons/bows/basicbow.json'], "items":['./items/potions/healthpotion.json', './items/potions/healthpotion.json']}
  elif info["class"] == "assassin":
    info["inventory"] = {"weapons:":['./weapons/daggers/basicdagger.json'], "items":['./items/potions/healthpotion.json', './items/potions/healthpotion.json']}
  elif info["class"] == "mage":
    info["inventory"] = {"weapons":['./weapons/staff/basicstaff.json'], "items":['./items/potions/healthpotion.json', './items/potions/healthpotion.json']}

  with open(info['inventory']["weapons"][0]) as f:
    weapon = json.load(f)
  typeEffect.medium("Since you chose the " + info["class"] + " class, you will be given a " + weapon["Name"].lower() + ", as well as 2 health potions.")
  typeEffect.slow("\nNow, it's time to begin...")
  sleep(1)
  clear()
  with open('./data/player.json', 'w') as f:
    f.write(json.dumps(info))
  return True