def get_longest_letters(string):

    letters=[]
    longest_letters=[]

    for i in range(len(string)):
        if(i==0 or string[i] >= string[i-1]): 
            letters.append(string[i])

        else:

            if len(letters) > len(longest_letters):   #check that  if the current list is the longest one and if so set it to longest
                 longest_letters = letters              
            letters=[]              #reset the list (because the order is different )to contain the  current letter  and start  again
            letters.append(string[i])

    if(len(letters)>=len(longest_letters)):
            longest_letters=letters 

    separator = ''
    output_letters = separator.join(longest_letters)
    print("The longest One is  : ",output_letters) 

  #  print ("The longest One is :: ",longest_letters)    #will print it as  a list 
        

    s=input("Please Enter any String you want :  ")

    get_longest_letters(s)




                