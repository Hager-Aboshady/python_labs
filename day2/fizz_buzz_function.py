def myfun (num):
    
     if(num%3==0 and num%5==0):
        print("FIZZ BUZZ")
     elif(num%5==0):
        print("BUZZ")
     elif(num%3==0):
        print("FIZZ") 
     else:
        print("This Number is not divisable by 3 nor 5 ")  
       



num=int(input("Please Enter a Number : "))
myfun(num)
 



