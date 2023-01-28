import sys

isbn = str(input("Enter the first 9 digits of an ISBN as a string: "))

if len(isbn) != 9 :
    print("Incorrect input. It must have exactly 9 digits")
    sys.exit()

tenDigit = (int(isbn[0]) * 1 + int(isbn[1]) * 2 + int(isbn[2]) * 3
+ int(isbn[3]) * 4 + int(isbn[4]) * 5 + int(isbn[5]) * 6 + int(isbn[6]) * 7
+ int(isbn[7]) * 8 + int(isbn[8]) * 9) % 11

if tenDigit == 10 :
    print("The ISBN-10 number is ", isbn, "X")
else:
    print("The ISBN-10 number is ", isbn, tenDigit)