# def is_email_exist(email):
#     try:
#         fileobj=open('users.txt','r')
#     except Exception as e:
#         return False
#     else:

#         for line in fileobj:
#             fields=line.strip().split(':')
#             print("hh")
#             print(fields)
#             email_field = fields[3]
#             if email_field==email:
#                 return True
#             else:
#                 print("This Email Doesn't Exist")    
            
#         # line=fileobj.readline()
#         # while line != '':
#         #     fields=line.split(':')
#         #     email_field=fields[3]
#         #     if email_field==email:
#         #         print("this email " ,email_field)
#         #         return True


              

#         # lines=fileobj.read()
#         # fields=lines.split(':')
#         # email_field = fields[3]
#         # for e in email_field:
#         #     if email_field==email:
#         #         print("This email")
#         #         return True
#         #     else:
#         #         print("nnnnooo")
#         return True 
       
#     finally:
#         fileobj.close()  

# is_email_exist('h@gmail.com')        
from getpass import getpass
password=getpass("Please Enter your password : ")
print(type(password))
