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
# from getpass import getpass
# password=getpass("Please Enter your password : ")
# print(type(password))



def delProj(ID):

    file=open('test.txt','r')
    allProj=file.readlines()
    #newlist=[]
    #counter=1

    # allProj = [proj for proj in allProj if not proj.startswith(str(ID))]

    projFile=open('test.txt','w')
    for proj in allProj:

        if proj.strip('\n').split(":")[0]==ID:
            print("before ",proj)
            #proj.strip('\n').split(":")[1]=input("Please Enter the Project's new title : ")
            newlist=proj.strip('\n').split(":")
            newlist[0]=input("kk")
            proj=":".join(newlist)
            print (newlist)

            #print("after ",proj.strip('\n').split(":")[0])
        projFile.write(proj)
            #counter=counter+1
        
        #projFile.write(str(allProj))
         
            
            

   
            





delProj("2")


# input text file
# inputFile = "test.txt"
# # Opening the given file in read-only mode.
# with open(inputFile, 'r') as filedata:
#    # Read the file lines using readlines()
#    inputFilelines = filedata.readlines()
#    # storing the current line number in a variable
#    lineindex = 1
#    # Enter the line number to be deleted
#    deleteLine = int(input("Enter the line number to be deleted = "))
#    # Opening the given file in write mode.
#    with open(inputFile, 'w') as filedata:
#       # Traverse in each line of the file
#       for textline in inputFilelines:
#          # Checking whether the line index(line number) is
#          # not equal to a given delete line number
#          if lineindex != deleteLine:
#             # If it is true, then write that corresponding line into file
#             filedata.write(textline)
#             # Increase the value of line index(line number) value by 1
#             lineindex += 1