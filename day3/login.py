from helpers import ask_for_num,ask_for_str,validate_email,is_email_exist,check_pass
from filesOperations import save_logged_user
from getpass import getpass
from termcolor import colored

def loginFun():

    print(colored(" Welcome Back \U0001F604 ","cyan"))

    
    
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
                    print(colored("Incorrect Passsword \U00002757 \U00002757 Please Try Again ","red"))
            break            

        else:
                print(colored("This Email Doesn't Exist \U00002757 \U00002757","red")) 


# loginFun()
  
                
                


    
    









