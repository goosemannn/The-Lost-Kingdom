from colorama import Fore
from time import sleep

def run(typeEffect, clear, hinput, startBattle, damage):

  green = Fore.GREEN 
  white = Fore.WHITE 
  currentlySelected = 0
  o1C = green 
  o2C = white 
  o3C = white 

  def updateOptions():
    nonlocal currentlySelected, o1C, o2C, o3C
    if currentlySelected == 1:
      o1C = green 
      o2C = white
      o3C = white
    elif currentlySelected == 2:
      o1C = white 
      o2C = green
      o3C = white
    elif currentlySelected == 3:
      o1C = white 
      o2C = white
      o3C = green

  def processInput(ch):
    nonlocal currentlySelected
    if ch == "s" and currentlySelected < 3:
      currentlySelected += 1 
      updateOptions()
    elif ch == "w" and currentlySelected > 1:
      currentlySelected -= 1
      updateOptions()
    elif ch == "enter":
      return 1

  def showOptions():
    clear()
    print("You wake up in a forest. You don't remember how you got there, you look around your area, but you don't find much of use, just some sticks and various stones. You notice a squirrel moving in the distance, but you don't bother to interact with it. Up above, you notice some birds flying through the sky. With no other leads to follow, you decide to go in the same direction as them. For a while, you just walk, nothing much happening. You start to get tired, and so you sit down for a few minutes. Out of seemingly nowhere, a small goblin appears. You aren't sure of it's intentions."+Fore.YELLOW+" What do you do?\n")
    print(o1C+'  Attack it')
    print(o2C+'  Talk to it')
    print(o3C+'  Ignore it'+Fore.WHITE)

  clear()
  typeEffect.medium("You wake up in a forest. You don't remember how you got there, you look around your area, but you don't find much of use, just some sticks and various stones. You notice a squirrel moving in the distance, but you don't bother to interact with it. Up above, you notice some birds flying through the sky. With no other leads to follow, you decide to go in the same direction as them. For a while, you just walk, nothing much happening. You start to get tired, and so you sit down for a few minutes. Out of seemingly nowhere, a small goblin appears. You aren't sure of it's intentions."+Fore.YELLOW+" What do you do?\n")
  typeEffect.medium(o1C+'  Attack it')
  typeEffect.medium(o2C+'  Talk to it')
  typeEffect.medium(o3C+'  Ignore it'+Fore.WHITE)

  while True:
    showOptions()
    j = hinput(processInput)
    if j == 1:
      break

  
  if currentlySelected == 1:
    typeEffect.medium("You ruthlessly attack the goblin.")
  elif currentlySelected == 2:
    typeEffect.medium("You try to talk to the goblin, but it doesn't seem to understand you. It eventually gets bored of trying to talk to you and attacks you.")
  elif currentlySelected == 3:
    typeEffect.medium("You ignore the goblin, and it doesn't appreciate that, so it attacks you.")
  
  sleep(3)
  goblin = {
    "name": "Goblin",
    "health": 20,
    "attacks": [['The Goblin hits you wtih a stick',5,"R"]]
  }
  startBattle(typeEffect, clear, hinput,damage,goblin)

 