from helpers import ask_for_num,ask_for_str,validate_email,is_email_exist,check_pass
from filesOperations import save_logged_user
from getpass import getpass

def loginFun():

    print(" Welcome Back !! ")

    
    
    while True:
        email=validate_email()
        if  is_email_exist(email):
            while True:
                password=getpass("Please Enter your password : ")
                
                if check_pass(password):
                    logged_user=f"{email}:{password}\n"
                    save_logged_user(logged_user)
                    break
                else:
                    print("Incorrect Passsword !! Please Try Again ")
            break            

        else:
                print("This Email Doesn't Exist") 


loginFun()
  
                
                


    
    









