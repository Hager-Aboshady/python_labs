#Write a program that generate a multiplication table from 1 to the number passed.


num = int(input("Enter a number: "))

list_of_lists = []

for i in range(num):
    
    list = []  #to create a new list
    
    for j in range(i+1):
        list.append((j+1)*(i+1))
    list_of_lists.append(list)

print(list_of_lists)