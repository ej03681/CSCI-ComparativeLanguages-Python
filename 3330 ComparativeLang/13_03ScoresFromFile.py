list = []
string = input("Enter a filename: ")
scoresFile = open("C:\\Users\\EddyJ\\" + string, "r")

scores = scoresFile.read().strip().split()

scoresFile.close()
sum = 0
for i in range(len(scores)):
    sum += int(scores[i])
    
avg = sum / len(scores)

print("There are ", len(scores), " scores")
print("The total is ", sum)
print("The average is ", round(avg, 2))