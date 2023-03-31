height = int(input("Enter pyramid height: "))


for row in range(height, 0, -1):
    
    spaces = " " * (row - 1)
    stars = "*" * (height - row + 1)

    
    print(spaces + stars)

