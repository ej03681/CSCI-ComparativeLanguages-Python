numberOfStudents = int(input("Enter the number of students: "))

highScore = 0
secondScore  = 0
secondName = ""
for i in range(numberOfStudents):
    name = input("Enter a student name: ")
    score = int(input("Enter a student score: "))
    if score > highScore :
        secondScore = highScore
        highScore = score
        secondName = name
        highestName = name
    elif score > secondScore:
        secondScore = score
        secondName = name
    
print("Top two students: ")
print(highestName, "'s score is",  highScore)
print(secondName, "'s score is", secondScore)