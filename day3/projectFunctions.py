import time
from helpers import *
from filesOperations import save_project


def createProj():
    title=input("Please Enter the Project's title : ")
    details=input("Please Enter the Project's details : ")
    totalTarget=ask_for_num("Please Enter the Project's total target : ")

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
    projectInfo=f"{title}:{details}:{totalTarget}:{startDate}:{endDate}:{current_email}:{time_id}\n"

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
                

    # projFile=open('projects.txt',"r")
    # print("Title:Details:total_target:st_date:end_date:created_by")
    # print(projFile.read())


# def deleteProj():
#     title=input("Please Enter the Project's title you want to edit : ")

#     allProj=viewProjs()
#     for proj in allProj:
#         print(proj.strip())





def search_using_time(time_id):
    allProj=viewProjs()
    for proj in allProj:
        if str(time_id)==proj.strip("\n").split(':')[6]:
            return True
        else:
            print("This Project doesn't exist !! ")
            return False





def editProjs():
    while True:
        title=input("Please Enter the Project's title you want to edit : ")
        if is_exist(title,0):
            if is_authorized():

            

                break
        
        else:
            print("This Project doesn't exist !! Please Try Again ")



    


# viewProjs()
# deleteProj()
#createProj()

# def is_email_exist(email):
#     try:
#         projFile=open('users.txt','r')
#     except Exception as e:
#         return False
#     else:

#         for line in projFile:
#             fields=line.strip().split(':')
#             email_field = fields[3]
#             if email_field==email:
#                 return True