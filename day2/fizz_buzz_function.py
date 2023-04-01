def myfun (num):
    
     if(num%3==0 and num%5==0):
        print("FIZZ BUZZ")
     elif(num%5==0):
        print("BUZZ")
     elif(num%3==0):
        print("FIZZ") 
     else:
        print("This Number is not divisable by 3 nor 5 ")  
       



num=input("Please Enter a Number : ")

if num.isdigit():
    num=int(num)
    myfun(num)
else:
    print("Invalid Input")

 



