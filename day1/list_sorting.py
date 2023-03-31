inList=[]
for i in range(5):
 userIN=input("Please Enter your List Element ")
 inList.append(userIN)


ascendingList=sorted(inList)
descendingList=sorted(inList,reverse=True)

print('Descending Order:' ,descendingList)

print('Ascending Order:' ,ascendingList)

