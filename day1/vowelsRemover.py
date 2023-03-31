userIn = input("Please Enter a String: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for char in userIn:
    if char in vowels:

         userIn=userIn.replace(char,'')
#        count += 1

print(userIn)
