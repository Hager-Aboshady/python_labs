#Write a program that prints the locations of "i" character in any string you added

text = input('Enter your String ')

# find the index of i
count=0
for char in text:
    if (char == 'i'):
       print("The index is ",count)
    count+=1

#enumerate