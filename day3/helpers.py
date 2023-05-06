import re
from termcolor import colored
import datetime
def ask_for_num(msg):
    while True:
      
        val=input(colored(msg,"yellow"))
        if val.isdigit():
            
            return int(val)
        else:
            print("Invalid Input \U00002757 \U00002757  . Please Try Again and Enter a valid number")

def ask_for_str(msg):
    while True:
        val = input(colored(msg, "yellow"))
        if val.isalpha():
            return val
        else:
            print(colored("Invalid input \U00002757 \U00002757  . Please Try Again and Enter a valid string", "red"))

def getProjs():
    try:
        projFile=open('projects.txt',"r")
    except Exception as e:
        print(colored('Error: Unable to open file \U00002757',"red"))
        return False
    else:
        return projFile.readlines()
                

def validate_email():
    while True:
        email = input(colored("Please enter your email address: ", "yellow"))
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        is_valid_email = re.match(email_regex, email)
        if is_valid_email:
            return email
        else:
            print(colored("Invalid email \U00002757 \U00002757 . Please Try Again and Enter a valid email address.", "red"))


def is_email_exist(email):
    try:
        fileobj=open('users.txt','r')
    except Exception as e:
        return False
    else:

        for line in fileobj:
            fields=line.strip().split(':')
            email_field = fields[3]
            if email_field==email:
                return True
 

    
       
    finally:
        fileobj.close()  


def check_pass(password):
    try:
        fileobj=open('users.txt','r')
    except Exception as e:
        return False
    else:

        for line in fileobj:
            fields=line.strip().split(':')
            pass_field = fields[4]

            if pass_field==password:
                return True
            

        
       
    finally:
        fileobj.close()          
                

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

     
def is_exist(ID):
    try:
        projFile=open('projects.txt','r')
    except Exception as e:
        return False
    else:

        allProj=projFile.readlines()
        for proj in allProj:
            if proj.strip('\n').split(":")[0]==str(ID):
                return True
            

 
def is_authorized(ID):
    try:
        projFile=open('projects.txt','r')
        userFile=open('logs.txt','r')

    except Exception as e:
        return False
    else:
        current_user=userFile.read()
      
        fields=current_user.split(":")
     
        current_email=fields[0]   #in login file
        #print (current_email)
     

        allProjs=projFile.readlines()
        
        for proj in allProjs:
           
            #print(proj.split(":")[6])
            if str(ID)==proj.split(":")[0] and proj.split(":")[6]==current_email:
               # print("hh")
               
                
                return True
        

# is_authorized()

# def is_email_exist(email):
# #     try:
# #         fileobj=open('users.txt','r')
# #     except Exception as e:
# #         print("cantt")
# #         return False
# #     else:
# #         import os

# #         file_path = 'myfile.txt'
# #         if os.stat('users.txt').st_size == 0:
# #             #print('File is empty')
# #             return True
# #         else:
# #             for line in fileobj:
# #                 fields=line.strip().split(':')
# #                 email_field = fields[3]
# #                 if email_field==email:
# #                     return True
# #            # print('File is not empty')