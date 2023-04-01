#Fill a list of 5 elements from the user, Sort it in descending and ascending orders then display the output.

inList=[]
for i in range(5):
 userIN=input("Please Enter your List Element ")
 inList.append(userIN)


ascendingList=sorted(inList)
descendingList=sorted(inList,reverse=True)

print('Descending Order:' ,descendingList)

print('Ascending Order:' ,ascendingList)

