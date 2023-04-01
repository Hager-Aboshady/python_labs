import random


name=input("Please Enter your Name to start the Game : ")

print(f"Welcome {name} to Hangman Game !")

words_list=['apple','elephant,','pizza','banana','hello','world','goat','tiger']

secret_word=random.choice(words_list)
	#Choose a random item from a sequence. Here seq can be a list, tuple, string, or any iterable like range.

turns=7

for i in range(len(secret_word)):
    print("_")
    
#while turns<=7:
    

