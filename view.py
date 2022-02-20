import os

def cls():
  os.system('cls')

def msgBox(msg):
  lines = msg.splitlines()  
  row  = get_max_str(lines)
  h = ''.join(['+'] + ['-' *(row+3)] + ['+'])
  print h
  for line in lines:
    l = ''.join(['| '] + [' ' *row] + [' |'])
    l = l[:2] + line + l[len(line) + 1:]
    print l
  print h

def output(msg):
  msg = msg + '\npress any key to continue:'
  msgBox(msg)
    
def get_max_str(lst):
    max_len = len(lst[0])   # list is not empty
    for x in lst:
        if len(x) > max_len:
            max_len = len(x)
    return max_len  