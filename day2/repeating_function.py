def repeatingFun():


    count = 0
    total = 0
    while True:
        userIn = input("Please enter a number or type 'done' to exit: ")
        if userIn.isdigit():
            userIn = int(userIn)
            count += 1
            total += userIn
        elif userIn.lower() == "done":
            break
        else:
            print("Invalid input")

    if count > 0:
        avg = total / count
        print(f"Number of counts are {count}")
        print(f"The total is {total}")
        print(f"The average is {avg}")
    else:
        print("No valid inputs were entered")





























    """
    count= 0
    total=0 
    avg=0

    userIn=input("Please Enter an Integer : ")
    
    while userIn.isdigit():
        l=list(userIn.split(" "))
        if len(l)==1:
            userIn=int(userIn)
            count=+1
            total=total+userIn
            avg=total/count
            userIn=("Please Enter another one : ")
        else:
            continue    

    if(userIn=="done" or userIn=="Done"):

        print(f"Number of Counts are {count}")
        print(f"The Total is  {total}")
        print(f"The average is  {avg}")

    """
 



repeatingFun()




       
