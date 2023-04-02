import random


name=input("Please Enter your Name to start the Game : ")

print(f"Welcome {name} to Hangman Game !")

#words_list=['apple','elephant,','pizza','banana','hello','world','goat','tiger']
words_list=['cat']

secret_word=random.choice(words_list)                   #Choose a random item from a the list 
	
turns=7 
#guessed_word=""   #
word_in_progress=''
letters=[]

# out_of_guess=False
# guess_count=0 #to count the number of your tries 

print("you are lookin for a word that number of letters are  :   ",end='')         #we assign end='' to print in the same line in Python 
    
for i in range(len(secret_word)):

    print(" _ ", end='')
    letters.append("_")  

print(" ")   

while turns > 0 :
        turns=turns-1
        
        guessed_letter=input("Guess and Enter a letter:  ")

        if(guessed_letter in secret_word ):
             # letters.append(guessed_letter)
             for i in secret_word:
                   if(secret_word[i]==guessed_letter):
                         letters[i]=guessed_letter

            
             print("You've guessed : ",str(letters)) 





    # =input("Guess and Enter a letter:  ")
    
    # turns=turns-1

    # if (guessed_word==secret_word):

    #      print(f" You win !! The word is {secret_word}")
    #      print(" Winner Winner Chicken Dinner !! ")
    #      break 
    #      #guess_count=+1

    # else:
    #     for i in secret_word:
    #         if()
    #         # if (i in guessed_word):
    #         #     word_in_progress+=i
    #         #     #print(word_in_progress)
    #         #     if (i not in word_in_progress_list):
    #         #         word_in_progress_list.append(i)

    #         # else:
    #         #    # dash="_"
    #         #   #  print("_",end='')
    #         #     word_in_progress+="_"


        print(word_in_progress)
       # turns=turns-1        






        
#print("You Guessed : " ,str(word_in_progress))        

        #guess_count=+1

# while turns<=7:
#     gussed_word=input("Guess and Enter the word :  ")

#     if (gussed_word==secret_word):

#         print(f" You win !! The word is {secret_word}")
#         print(" Winner Winner Chicken Dinner !! ")

        

        

    # if (len(gussed_word)==len(secret_word)):
    #     for i in range(len(secret_word)):
    #         for j in range(len(gussed_word)):
    #             if(gussed_word[i]==secret_word[j]):
    #                 list_index=[]
    #                 list_index.append(i)
    #                  #after_guess=
                    
    #                #cur_sub+=string[i]



    
