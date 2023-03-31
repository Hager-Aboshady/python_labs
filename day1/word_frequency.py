
userIN = input("Enter a String ")
count = 0

for i in range(len(userIN) - 2):
    
    if userIN[i:i+3] == 'iti':

        count += 1

# Print the final count
print("Number of frequency times is :: ", count)

