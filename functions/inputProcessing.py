import msvcrt

def hinput(hook):
  char = msvcrt.getch().decode("utf-8")
  if char == '\r':
    return hook("enter")
  else:
    return hook(char)
  