import json
from colorama import Fore

def startBattle(typeEffect, clear, hinput, damage, enemy:dict):
  with open("./data/player.json", "r") as f:
    player = json.load(f)

  white = Fore.WHITE
  green = Fore.GREEN
  actionSelected = 1
  fC = green 
  iC = white 
  sC = white 

  weaponSelected = 1

  def updateOptions():
    nonlocal white, green, actionSelected, fC, iC, sC
    if actionSelected == 1:
      fC = green
      iC = white
      sC = white
    elif actionSelected == 2:
      fC = white
      iC = green
      sC = white
    elif actionSelected == 3:
      fC = white
      iC = white
      sC = green
      
  
  def inputProcessing(inp):
    nonlocal actionSelected
    if inp == 'a' and actionSelected > 1:
      actionSelected -= 1
      updateOptions()
      return False 
    elif inp == "d" and actionSelected < 3:
      actionSelected += 1
      updateOptions()
      return False
    elif inp == "enter":
      return True
  
  def showFight():
    clear()
    nonlocal player, fC, iC, sC, green, white, enemy
    if player["health"] > 50:
      print(Fore.BLUE+"Your HP: "+Fore.GREEN+str(player["health"]))
    elif player["health"] > 15:
      print(Fore.BLUE+"Your HP: "+Fore.YELLOW+str(player["health"]))
    else:
      print(Fore.BLUE+"Your HP: "+Fore.RED+str(player["health"]))
  
    print("")  
    if enemy["health"] > 50:
      print(Fore.LIGHTBLACK_EX+enemy["name"]+"'s HP: "+Fore.GREEN+str(enemy["health"]))
    elif enemy["health"] > 15:
      print(Fore.LIGHTBLACK_EX+enemy["name"]+"'s HP: "+Fore.YELLOW+str(enemy["health"]))
    else:
      print(Fore.LIGHTBLACK_EX+enemy["name"]+"'s HP: "+Fore.RED+str(enemy["health"]))

    print("")
    print(fC+"---------"+(green+"+" if fC == green or iC == green else white+"+")+iC+"---------"+(green+"+" if iC==green or sC==green else white+"+")+sC+"---------")
    print(fC+"| ATTACK "+(green+"|" if fC==green or iC==green else white+"|")+iC+"   USE   "+(green+"|" if iC==green or sC==green else white+"|")+sC+" PARDON |")
    print(fC+"---------"+(green+"+" if fC == green or iC == green else white+"+")+iC+"---------"+(green+"+" if iC==green or sC==green else white+"+")+sC+"---------") 

  def showWeapons():
    nonlocal green, white
    clear()
    print("------WEAPONS------")
    i = 1
    for item in player["inventory"]["weapons"]:
      with open(item, "r") as f:
        weapon = json.load(f)
      if weaponSelected == i:
        print(green+"  -"+weapon["Name"])
        print("     -"+weapon["Description"])
      else:
        print(white+"  -"+weapon["Name"])
    print(Fore.RED+"Back")
      
  def weaponSelectInp(inp):
    if inp == "s" and weaponSelected < len(player["inventory"]["weapons"]):
      weaponSelected += 1
      return False
    elif inp == "w" and weaponSelected > 1:
      weaponSelected -= 1
      return False
    elif inp == "enter":
      return True
  
  while True: 
    showFight()
    if hinput(inputProcessing):
      break

  if actionSelected == 1:
    while True:
      while True:
        showWeapons()
        if hinput(weaponSelectInp):
          break
      if weaponSelected == len(player["inventory"]["weapons"]):
        continue 
      break 
    clear()
    enemy["health"] = damage(enemy["health"], player["inventory"]["weapons"][weaponSelected-1]["dmg"][0], player["inventory"]["weapons"][weaponSelected-1]["dmg"][1])
    typeEffect.medium("You attack the " + enemy["name"] + " with your " + player["inventory"]["weapons"][weaponSelected-1] + ", leaving it with " + str(enemy["health"]) + " HP.")
    
      
  elif actionSelected == 2:
    pass 
  elif actionSelected == 3:
    pass

  

  
    

  

