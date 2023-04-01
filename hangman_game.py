import random


name=input("Please Enter your Name to start the Game : ")

print(f"Welcome {name} to Hangman Game !")

words_list=['apple','elephant,','pizza','banana','hello','world','goat','tiger']


secret_word=random.choice(words_list)                   #Choose a random item from a the list 
	

turns=7
print("The Secret word consists of  ",end='')         #we assign end='' to print in the same line in Python 
    


for i in range(len(secret_word)):

    print(" _ ", end='')

print(" ")    
#while turns<=7:
    
