
#Write a program that counts up the number of vowels [a, e, i, o,u] contained in the string.

userIn = input("Please Enter a String: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for char in userIn:
    if char in vowels:
        count += 1

print("The number of vowels in your input string is:", count)
