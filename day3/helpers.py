import re
import datetime
from projectFunctions import viewProjs
def ask_for_num(msg):
    while True:
      
        val=input(msg)
        if val.isdigit():
            
            return int(val)
        else:
            print("Invalid Input. Please try again and enter a valid number")



def ask_for_str(msg):
    while True:
      
        val=input(msg)
        if val.isalpha():
            
            return (val)
        else:
            print("Invalid Input. Please try again and enter a valid string")


def validate_email():
    while True:
    
        email = input("Please enter your email address: ")
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        is_valid_email = re.match(email_regex, email)
        if is_valid_email:
            return email
        else:
            print("Invalid email. Please enter a valid email address: ")



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

     
def is_exist(val,fieldNo):
    allProjs=viewProjs()
    for proj in allProjs:
        if proj[fieldNo]==val:
            return True
        



    # try:
    #     projFile=open(filePath,'r')
    # except Exception as e:
    #     return False
    # else:

    #     for line in projFile:
    #         fields=line.strip().split(':')
    #         fieldVal = fields[fieldNo]
    #         if fieldVal==val:
    #             return True
            
 
def is_authorized():



    try:
        # projFile=open('projects.txt','r')
        userFile=open('users.txt','r')

    except Exception as e:
        return False
    else:
        current_user=userFile.read()
        fields=current_user.split(":")
        current_email=fields[0]

        allProjs=viewProjs()
        for proj in allProjs:
            if proj[5]==current_email:
                return True
        



        # for line in projFile:
            
        #     fields=line.strip().split(':')
        #     createdBy_field = fields[5]
        #     counter=counter+1

        #     if createdBy_field==current_email:
        #         return True       
