list = []

scoresFile = open("C:\\Users\\EddyJ\\Scores.txt", "r")

scores = scoresFile.read().strip().split()

scoresFile.close()
sum = 0
min = float(scores[0])

less = []
for i in range(len(scores)):
    sum += float(scores[i])
    if min > float(scores[i]):
        min = float(scores[i]) 
    if float(scores[i]) < 100:
        less.append(float(scores[i]))
 
max = max(scores)
avg = sum / len(scores)


print("Minimum value is ", min)
print("Max value is ", max)
print("There are ", len(scores), " scores")
print("The total is ", sum)
print("The average is ", round(avg, 2))
print("The values less than 100 are ", less)