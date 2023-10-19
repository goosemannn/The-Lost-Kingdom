import getch

def hinput(hook):
  char = getch.getch()
  print(char)
  if char == '\n':
    return hook("enter")
  else:
    return hook(char)
  