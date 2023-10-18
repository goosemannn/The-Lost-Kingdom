# Imports
import sys
import json
import os

# Project Imports 
import stages.intro as intro
import stages.tutorial as tutorial
import stages.beginning as beginning
import functions.typeEffect as typeEffect
from functions.clear import clear

with open("./data/stagesComplete.json", "r") as f:
  stagesComplete = json.load(f)
  f.close()

def updateStagesComplete():
  global stagesComplete
  stagesComplete["stagesCompleted"] += 1
  with open('./data/stagesComplete.json', 'w') as f:
    f.write(json.dumps(stagesComplete))
  


# Tutorial 
if stagesComplete["stagesCompleted"] < 1:
  tutorial.run(typeEffect, clear)
  updateStagesComplete()

# Intro
if stagesComplete["stagesCompleted"] < 2:
  intro.run(typeEffect, clear)
  updateStagesComplete()

# After the intro, the game starts
if stagesComplete["stagesCompleted"] < 3:
  beginning.run(typeEffect)
  updateStagesComplete()

