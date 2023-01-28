import sys
number = int(input("Enter an integer, the input end if it is 0: "))
positive = 0
negative = 0
count = 0
total = 0
if number == 0:
    print("You didn't enter any number")
    sys.exit()
while number != 0:
    total += number
    if number > 0 :
        positive += 1
    elif number < 0:
        negative += 1
    count += 1
    number = int(input("Enter an integer, the input end if it is 0: "))
print("The number of positives is ", positive)
print("The number of negatives is ", negative)
print("The total is ", total)
print("The average is ", total / count)