import sys
from time import sleep

def fast(text):
  text += "\n"
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.015)

def slow(text):
  text += "\n"
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.045)


def medium(text):
  text += "\n"
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.03)