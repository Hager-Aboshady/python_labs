from helpers import ask_for_num
from termcolor import colored
from projectFunctions import *


def goToSecMenu():
    print(colored(" --- To Create new project press 1 --- ", "yellow"))
    print(colored(" --- To View all projects press 2 ---", "yellow"))
    print(colored(" --- To Update an existing project press 3 --- ", "yellow"))
    print(colored(" --- To Delete an existing project press 4 ----", "yellow"))
    print(colored(" --- To Go back to the main menu press 0 ----", "green"))
    while True:
        choice = ask_for_num("Enter your choice: ")
        if choice==1:
            createProj()
        elif choice==2:
            viewProjs()
        elif choice==3:
            editProj()
        elif choice==4:
            delProj()
        elif choice==0:
            break
        else:
            print(colored("Invalid Input \U00002757\U00002757 Please choose from 0 - 4", "red"))







