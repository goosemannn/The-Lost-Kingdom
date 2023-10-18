from colorama import Fore

def run(typeEffect):
  typeEffect.medium("You wake up in a forest. You don't remember how you got there, you look around your area, but you don't find much of use, just some sticks and various stones. You notice a squirrel moving in the distance, but you don't bother to interact with it. Up above, you notice some birds flying through the sky. With no other leads to follow, you decide to go in the same direction as them. For a while, you just walk, nothing much happening. You start to get tired, and so you sit down for a few minutes. Out of seemingly nowhere, a small goblin appears. You aren't sure of it's intentions."+Fore.YELLOW+" What do you do?")
  typeEffect.medium(Fore.RED+'  A. Attack it')
  typeEffect.medium(Fore.BLUE+'  B. Talk to it')
  typeEffect.medium(Fore.GREEN+'  C. Ignore it'+Fore.WHITE)
  while True:
    choice = input('|>')
    if choice == 'A':
      typeEffect.medium("You ruthlessly attack the goblin.")
      # Figure out fight system
      break
    elif choice == 'B':
      typeEffect.medium("You try and talk to the goblin, but it doesn't seem to understand you. Eventually, it gets bored and attacks you.")
      # Figure out fight system
      break
    elif choice == 'C':
      typeEffect.medium("You try and ignore the goblin, but it attacks you anyway")
      #Figure out fight system
      break
    else:
      typeEffect.slow("You know that isn't an option. Try again.")
 