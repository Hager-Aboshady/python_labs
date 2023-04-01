def revFun(word):
    return word[::-1]


word=input("Please Enter a Word : ")

while not word or word.isdigit():
    word=input("Invalid Input .Please Enter a Word : ")


revWord=revFun(word)
print(f"Your Word Before Reversing is {word} and After Reversing is {revWord} ")
    