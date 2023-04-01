


def longest_sub(string):

    longest=''
    cur_sub=''

    for i in range(len(string)):
        if (i==0,string[i]>= string[i-1]):
            cur_sub+= string[i]

        else:
            if (len(longest) > len (cur_sub)) :
            
                longest=cur_sub
                cur_sub+=string[i]

    if len(cur_sub) > len(longest):
        longest = cur_sub

    print("Longest substring in alphabetical order is:", longest)           

      
string=input("Please Enter any String you want :  ")

longest_sub(string)




                