import json
from colorama import Fore

class FightSystem:
  def __init__(enemy):
    with open("./data/player.json", "r") as f:
      player = json.load(f)

    white = Fore.WHITE
    green = Fore.GREEN
    actionSelected = 0
    fC = green 
    iC = white 
    sC = white 

    showFight(enemy, player, actionSelected, fC, iC, sC, green, white)
    while True: 
      pass 
      # Figure out how to get menu select to work

  def showFight(enemy:dict, player:dict, actionSelected, fC, iC, sC, green, white):
    if player["health"] > 50:
      print(Fore.BLUE+"Your HP: "+Fore.GREEN+str(player["health"]))
    elif player["health"] > 15:
      print(Fore.BLUE+"Your HP: "+Fore.YELLOW+str(player["health"]))
    else:
      print(Fore.BLUE+"Your HP: "+Fore.RED+str(player["health"]))
  
    print("/n")
    if enemy["health"] > 50:
      print(Fore.LIGHTBLACK_EX+enemy["name"]+"'s HP: "+Fore.GREEN+str(enemy["health"]))
    elif enemy["health"] > 15:
      print(Fore.LIGHTBLACK_EX+enemy["name"]+"'s HP: "+Fore.YELLOW+str(enemy["health"]))
    else:
      print(Fore.LIGHTBLACK_EX+enemy["name"]+"'s HP: "+Fore.RED+str(enemy["health"]))

    print(fC+"---------"+(green+"+" if fC == green or iC == green else white+"+")+iC+"---------"+(green+"+" if iC==green or sC==green else white+"+")+sC+"---------")
    print(fC+"| ATTACK "+(green+"|" if fC==green or iC==green else white+"|")+iC+" ITEM "+(green+"|" if iC==green or sC==green else white+"|")+sC+" SPARE |")
    print(fC+"---------"+(green+"+" if fC == green or iC == green else white+"+")+iC+"---------"+(green+"+" if iC==green or sC==green else white+"+")+sC+"---------")  
  

  
    

  

