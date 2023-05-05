import time
from helpers import *
import uuid
from filesOperations import save_project


def createProj():
    title=input("Please Enter the Project's title : ")
    details=input("Please Enter the Project's details : ")
    totalTarget=input("Please Enter the Project's total target : ")

    while True:
        
        startDate=input("Please Enter the start date in 'YYYY-MM-DD' format : ")
        if is_valid_date(startDate):
            break
        else:
            print("Invalid Date Format !! Please Try Again  ")

    while True:
        
        endDate=input("Please Enter the end date in 'YYYY-MM-DD' format : ")
        if is_valid_date(endDate):
            break
        else:
            print("Invalid Date Format !! Please Try Again  ")            


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
        projFile=open('users.txt',"r")
    except Exception as e:
        return False
    else:
        print("Title:Details:total_target:st_date:end_date:created_by")
        print(projFile.read())
        return projFile.readlines()
                


def delProj():
    while True:
        ID=input("Please Enter the Project's ID you want to delete : ")
        if is_exist(ID):
           
            if is_authorized():
                
                allProj=getProjs()
                projFile=open('projects.txt','w')
                for proj in allProj:
                    if  proj.strip('\n').split(":")[0]!=str(ID):
                        projFile.write(proj)
                break
            else:
                print("You are not authorized to delete this projet \U0001F512")        
                 

        
        else:
            print("This Project doesn't exist !! Please Try Again ")

def editProj():
    while True:
        ID=input("Please Enter the Project's ID you want to edit : ")
        if is_exist(ID):
           
            if is_authorized():
                
                allProj=getProjs()
                projFile=open('projects.txt','w')
                for proj in allProj:
                    if  proj.strip('\n').split(":")[0]==str(ID):
                        # projFile.write(proj)
                        list=proj.strip('\n').split(":")

                        list[1]=input("Please Enter the Project's new title : ")
                        list[2]=input("Please Enter the Project's new details : ")
                        list[3]=input("Please Enter the Project's new total target : ")
                        proj=":".join(list)
                        



                    projFile.write(proj)
                break
            else:
                print("You are not authorized to edit this projet \U0001F512")        
                 

        
        else:
            print("This Project doesn't exist \U0001F625 !! Please Try Again ")
#createProj()
#editProj()
#delProj()


#delProj()
#createProj()


def search_using_time():
    while True:
        time_id=ask_for_num("Please Enter the time you want to search by \U0001F55B : ")
        allProj=getProjs()

        for proj in allProj:
            if str(time_id)==proj.strip("\n").split(':')[7]:
                print("--------Search Results-------\U0001F440")
                print(proj)
                
                break
            else:
                print("--------Search Results------- \U0001F440")
                print("This Project doesn't exist \U0001F625 ")
                


