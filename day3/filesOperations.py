def save_user_data(userInfo):
    try:
        fileobj=open('users.txt','a')
    except Exception as e:
        return False
    else:
        fileobj.write(userInfo)
        print("New user Data has been added Successfully \U0001F44D")
        return True  
    finally:
        fileobj.close()  

def save_logged_user(logged_user):
    try:
        fileobj=open('logs.txt','w')
    except Exception as e:
        return False
    else:
        fileobj.write(logged_user)
        # print("New user Data has been added \U0001F44D")
        return True  
    finally:
        fileobj.close()          



def save_project(proj_info):
    try:
        projFile=open('projects.txt','a')
    except Exception as e:
        return False
    else:
        projFile.write(proj_info)
        print("New Project has been added Successfully \U0001F44D")
        return True  
    finally:
        projFile.close()      
