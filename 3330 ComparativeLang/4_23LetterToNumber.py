letter = str(input("Enter a letter: "))

letter = letter.upper()
value = 0
if letter == 'A' :
    print("The numeric value for grade ", letter, " is 4")
elif letter == 'B':
    print("The numeric value for grade ", letter, " is 3")
elif letter == 'C':
    print("The numeric value for grade ", letter, " is 2")
elif letter == 'D':
    print("The numeric value for grade ", letter, " is 1")
elif letter == 'F':
    print("The numeric value for grade ", letter, " is 0")
else :
    print(letter, " is invalid grade")