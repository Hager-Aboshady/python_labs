from registeration import registerFun
from login import loginFun
from helpers import ask_for_num

def mainMenu():
    print("Welcome to Crowd-Funding \U0001F604")
    while True:
        choice=ask_for_num("To Register Please Enter 1 , To login Please Enter 2 , To exit Enter 0 ")
        if(choice==1):
            registerFun()
           # print("r")
        elif(choice==2):
            loginFun()
            
            #print("l")

        elif(choice==0):
            print("see you later \U0001F44B")
            break
        

        else:
            print(" Please Enter 1 or 2 ")   


mainMenu()

        

