from helpers import ask_for_num,ask_for_str,validate_email,is_email_exist
import re
import uuid
import time
from filesOperations import *
from getpass import getpass

def registerFun():
   print("You Want to Join us ? We're so grateful !! \U0001F929")


   fname=ask_for_str("Please Enter Your First Name : ")
   lname=ask_for_str("Please Enter Your Last Name : ")
   while True:
    email=validate_email()
    if is_email_exist(email):
        print("This Email is already exist")
        continue
    else:    
        password=validate_pass()
        confirmed_password=confirm_pass(password)
        phone_num=validate_phone_number()
        id = uuid.uuid4()    # Generate a UUID
        time_id=round(time.time())

        user_info=f"{id}:{fname}:{lname}:{email}:{password}:{phone_num}:{time_id}\n"

        save_user_data(user_info)
        break
 



def validate_pass():
    while True:

        password=getpass("Please Enter your Password: ")
        if len(password) >= 8:
            return password
        else:
            print("Please Try Again ! Your Password has to contain at least 8 Characters .")


def confirm_pass(password_to_confirm):
    while True:
        password=getpass("Please Enter your Password Again : ")
        if(password_to_confirm== password):
            return password
        else:
            print("Please Try Again ! The Password Confirmation doesn't match .")



def validate_phone_number():
    while True:
        number=ask_for_num("Please Enter Your Phone Number : ")
     
        # print(len(str(number)))
        # fchar=str(number)[0]
        # print(fchar)
     

        if len(str(number))== 10 :
            # print("hhh")
            return number

        else:
            print(" The length of Phone number must be 10 digits and start with 0 ")
        
           
# registerFun()



