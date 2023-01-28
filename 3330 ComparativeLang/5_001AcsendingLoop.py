count = 0
tempN = 0
isAscending = True 

number = int(input("Enter six numbers: "))
for i in range(5):
    number = int(input())
    if number > tempN :
        tempN = number
    else :
        isAscending = False
print(isAscending)