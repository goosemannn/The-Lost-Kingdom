import random
import json
from colorama import Fore
from time import sleep

def damage(weapon, enemy, typeEffect, clear, hinput, health, attackType, damage, hitChance, spells=[], bleeding=False):

  spellSelected = 0
  def inputProcessing(inp):
    nonlocal spellSelected, spells
    if inp == "s" and spellSelected < len(spells):
      spellSelected += 1
      return False
    elif inp == "w" and spellSelected > 0:
      spellSelected -= 1
      return False
    elif inp == "enter":
      return True

  def showSpells():
    nonlocal spellSelected, spells 
    clear()
    print("------SPELLS------")
    i = 0
    for s in spells:
      with open(s, "r") as f:
        spell = json.load(f)
      if i == spellSelected:
        print(Fore.GREEN+"  -" + spell["Name"])
        print(Fore.GREEN+"     -"+spell["Description"]+Fore.WHITE)
      else:
        print(Fore.WHITE+"  -" + spell["Name"])
      i += 1
        
    
  if random.randint(0, 100) > hitChance:
    return health, "Mi"
  
  if attackType == "R":
    typeEffect.medium(Fore.WHITE+"You attack the " + enemy["name"] + " with your " + weapon["Name"] + ", leaving it with " + str(enemy["health"]) + " HP.")
    sleep(2)
    clear()
    return health-damage, "R"
  elif attackType == "C":
    if random.randint(0, 100) > 80: 
      typeEffect.medium(Fore.WHITE+"Critical Hit! You attack the " + enemy["name"] + " with your " + weapon["Name"] + ", leaving it with " + str(enemy["health"]) + " HP.")
      sleep(2)
      clear()
      return health-(damage*1.75), "R"
    else: return health-damage, "C"
  elif attackType == "B" and not bleeding:
    typeEffect.medium(Fore.WHITE+"You attack the " + enemy["name"] + " with your " + weapon["Name"] + ", leaving it with " + str(enemy["health"]) + " HP and bleeding.")
    sleep(2)
    clear()
    return health-damage, "B"
  elif attackType == "B" and bleeding:
    return health-(damage*.3), "B"

  elif attackType == "M":
    clear()
    while True:
      showSpells()
      if hinput(inputProcessing):
        break 
    with open(spells[spellSelected], 'r') as f:
      spell = json.load(f)
    if random.randint(0, 100) > spell["hitChance"]:
      return 0, "M"    
    if spell["Effect"][0] == "dmg":
      if spell["Effect"][1][0] == "R" or spell["Effect"][1][0] == "B":
        typeEffect.medium(Fore.WHITE+"You attack the " + enemy["name"] + " with your " + spell["Name"] + ", leaving it with " + str(enemy["health"]) + " HP.")
        sleep(2)
        clear()
        return health-spell["Effect"][1][1], spell["Effect"][1][0]
      elif spell["Effect"][1][0] == "C":
        if random.randint(0, 100) > 80: 
          typeEffect.medium(Fore.WHITE+"Critical Hit! You attack the " + enemy["name"] + " with your " + spell["Name"] + ", leaving it with " + str(enemy["health"]-(spell["Effect"][1][1]*1.75)) + " HP.")
          sleep(2)
          clear()
          return health-(spell["Effect"][1][1]*1.75), spell["Effect"][1][0]
        else: 
          typeEffect.medium(Fore.WHITE+"You attack the " + enemy["name"] + " with your " + spell["Name"] + ", leaving it with " + str(enemy["health"]-spell["Effect"][1][1]) + " HP.")
          sleep(2)
          clear()
          return health-spell["Effect"][1][1], spell["Effect"][1][0]
        
        
      
      
        
        
    
  
    