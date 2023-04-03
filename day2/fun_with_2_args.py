list=[]
def myfun (length,start):
    num=start
    for i in range(length):
        list.append(num)
        num=num+1


l=int(input("please enter the length of you list : "))
s=int(input("please enter the number you want to start from : "))

myfun(l,s)
print("your list is: ",list)

        
