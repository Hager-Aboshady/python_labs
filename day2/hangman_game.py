import random

name=input("Please Enter your Name to start the Game : ")

print(f"Welcome {name} to Hangman Game !")

#words_list=['apple','elephant,','pizza','banana','hello','world','goat','tiger','cat ']
words_list=['cat']

secret_word=random.choice(words_list)                               #Choose a random item from a the list 
	
turns=7 
letters=[]

print("you are looking for a word that consists of :   ",end='')   #we assign end='' to print in the same line in Python 
    
for i in range(len(secret_word)):

    print(" _ ", end='')
    letters.append(" _ ")  

print(" ")   

while turns > 0 :
        
        
        guessed_letter=input("Guess and Enter a letter:  ")

        if(guessed_letter in secret_word ):
             
             for i in range(len(secret_word)):
             
                   if(secret_word[i]==guessed_letter):
                         letters[i]=guessed_letter         #access this index and replace it => replace _ with this letter 

             if(" _ "  not in letters):
                   print(" Congratulations !! You Win ! ")
                   
                   break
        elif(guessed_letter in letters):
              print("This letter is already exist !! ")
        else:
              turns=turns-1

        separator = ''
        output_letters = separator.join(letters)
        print(f"{turns} turns left ")
        print("You've guessed until now : ",output_letters)  



if(" _ "  in letters):
    print("You Lose, Game Over")
    

print("The Secret Word was : " ,secret_word)
    
