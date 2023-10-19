import random

def damage(health, attackType, damage, hitChance, bleeding=False):
  
  if attackType == "R":
    return health-damage, "R"
  elif attackType == "C":
    if random.randint(0, 100) > 80: return health-(damage*1.75), "R"
    else: return health-damage, "C"
  elif attackType == "B" and not bleeding:
    return health-damage, "B"
  elif attackType == "B" and bleeding:
    return health-(damage*.3), "B"
  
    