import view
import model

def showMenu():
  selection = -1
  while (selection != 0):
    view.msgBox('Select a option:\n1. Say hello to user #1\n2. Say hello to user #2\n0. Exit\n')
    try: selection = int(input())
    except: selection = -1       
    if    selection == 1: view.output('Hi '+model.say_hello(0)+'!')                    
    elif  selection == 2: view.output('Hi '+model.say_hello(1)+'!')                    
    elif  selection == 0: view.output('Bye bye')                
    else: view.output('Wrong option')        
    raw_input()
    view.cls()

showMenu()  
