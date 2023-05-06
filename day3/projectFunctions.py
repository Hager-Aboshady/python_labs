import time
from helpers import *
import uuid
from prettytable import PrettyTable
from filesOperations import save_project


def createProj():
    title=input(colored("Please Enter the Project's title : ","yellow"))
    details=input(colored("Please Enter the Project's details : ","yellow"))
    totalTarget=ask_for_num("Please Enter the Project's total target : ")

    while True:
        
        startDate=input(colored("Please Enter the start date in 'YYYY-MM-DD' format : ","yellow"))
        if is_valid_date(startDate):
            break
        else:
            print("Invalid Date Format \U00002757 \U00002757  Please Try Again  ")

    while True:
        
        endDate=input(colored("Please Enter the end date in 'YYYY-MM-DD' format : ","yellow"))
        if is_valid_date(endDate):
            break
        else:
            print("Invalid Date Format \U00002757 \U00002757  Please Try Again  ")            


    logsFile=open('logs.txt',"r")
    current_user=logsFile.read()
    fields=current_user.split(':')
    current_email=fields[0]
    time_id=round(time.time())
    ID= uuid.uuid4()  
    projectInfo=f"{ID}:{title}:{details}:{totalTarget}:{startDate}:{endDate}:{current_email}:{time_id}\n"

    save_project(projectInfo)



def viewProjs():
    try:
        projFile = open('projects.txt', 'r')
    except:
        print(colored('Error: Unable to open file \U00002757',"red"))
        return False

    proj_table = PrettyTable()
    proj_table.field_names = ['ID', 'Title', 'Details', 'Total Target', 'Start Date', 'End Date', 'Created By']

    for line in projFile:
        proj = line.strip().split(':')
        proj_table.add_row([proj[0], proj[1], proj[2], proj[3], proj[4], proj[5], proj[6]])

    print(proj_table)




def delProj():
    while True:
        ID=input("Please Enter the Project's ID you want to delete or 0 to Exit : ")
        if ID!="0":
            if is_exist(ID):
            
                if is_authorized(ID):
                    
                    allProj=getProjs()
                    projFile=open('projects.txt','w')
                    for proj in allProj:
                        if  proj.split(":")[0]!=str(ID):
                            projFile.write(proj)
                    break
                else:
                    print(colored("You are not authorized to delete this projet \U0001F512","red"))     
                    

            
            else:
                print("This Project doesn't exist 	\U00002757 \U00002757  Please Try Again ")
        else:
            break

def editProj():
    while True:
        ID=input(colored("Please Enter the Project's ID you want to edit ot 0 to Exit : ", 'blue'))
        if ID!="0":
            if is_exist(ID):
            
                if is_authorized(ID):
                    
                    allProj=getProjs()
                    projFile=open('projects.txt','w')
                    for proj in allProj:
                        if  proj.split(":")[0]==str(ID):
                            # projFile.write(proj)
                            list=proj.split(":")

                            list[1]=input(colored("Please Enter the Project's new title : ", 'yellow'))
                            list[2]=input(colored("Please Enter the Project's new details : ", 'yellow'))
                            list[3]=input(colored("Please Enter the Project's new total target : ", 'yellow'))
                            proj=":".join(list)


                        projFile.write(proj)
                    break
                else:
                    print("You are not authorized to edit this projet \U0001F512")        
                    

            
            else:
                print("This Project doesn't exist \U0001F625 !! Please Try Again ")
        else :
            break       



def search_using_time():
    while True:
        time_id = ask_for_num("Please Enter the time you want to search by or 0 to Exit \U0001F55B : ")
        if time_id!="0":
            allProj = getProjs()

            for proj in allProj:
                if str(time_id) == proj.strip("\n").split(':')[7]:
                    print(colored("--------Search Results-------\U0001F440", "green"))
                    print(colored(proj, "blue"))
                    break
                else:
                    print(colored("--------Search Results------- \U0001F440", "green"))
                    print(colored("This Project doesn't exist \U0001F625", "red"))
                    break

        else:
            break        


