#Write a program that remove all vowels from the input word and generate a brief version of it.



userIn = input("Please Enter a String: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for char in userIn:
    if char in vowels:

         userIn=userIn.replace(char,'')


print(userIn)
