import re
import datetime
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

def getProjs():
    try:
        projFile=open('projects.txt',"r")
    except Exception as e:
        return False
    else:
        return projFile.readlines()
                


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

     
def is_exist(ID):
    # allProjs=viewProjs()
    # for proj in allProjs:
    #     if proj[fieldNo]==val:
    #         return True
        

    try:
        projFile=open('projects.txt','r')
    except Exception as e:
        return False
    else:

        allProj=projFile.readlines()
        for proj in allProj:
            if proj.strip('\n').split(":")[0]==str(ID):
                return True
            
            # fields=line.strip().split(':')
            # fieldVal = fields[fieldNo]
            # if fieldVal==val:
            #     return True
            
 
def is_authorized():
    try:
        projFile=open('projects.txt','r')
        userFile=open('logs.txt','r')

    except Exception as e:
        return False
    else:
        current_user=userFile.read()
        #print(current_user)
        fields=current_user.split(":")
        #print(fields)
        current_email=fields[0]   #in login file
        #print(current_email)

        allProjs=projFile.readlines()
        
        for proj in allProjs:
            #print (proj)
            if proj.strip('\n').split(":")[6]==current_email:
                #print("hhhggg")
                return True
        


# is_authorized()
        # for line in projFile:
            
        #     fields=line.strip().split(':')
        #     createdBy_field = fields[5]
        #     counter=counter+1

        #     if createdBy_field==current_email:
        #         return True       
