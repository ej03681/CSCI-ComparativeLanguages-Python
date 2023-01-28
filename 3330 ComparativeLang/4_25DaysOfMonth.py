import sys
year = int(input("Enter a year: "))
month = str(input("Enter a month: "))
nMonth = 0

if month == 'Jan' :
    nMonth = 1
elif month == 'Feb' :
    nMonth = 2
elif month == 'Mar' :
    nMonth = 3
elif month == 'Apr' :
    nMonth = 4
elif month == 'May' :
    nMonth = 5
elif month == 'Jun' :
    nMonth = 6
elif month == 'Jul' :
    nMonth = 7
elif month == 'Aug' :
    nMonth = 8 
elif month == 'Sep' :
    nMonth = 9
elif month == 'Oct' :
    nMonth = 10
elif month == 'Nov' :
    nMonth = 11
elif month == 'Dec' :
    nMonth = 12
else: 
    print(month, " is not correct month name")
    sys.exit()

days = 0
if year % 4 == 0 and nMonth == 2:
    days = 29
else :
    days = int(28 + (nMonth + (nMonth / 8)) % 2 + 2 % nMonth + 2 * (1 // nMonth))
    
if 1 > nMonth > 12 :
    print("Enter month 1- 12")
elif nMonth == 1 :
    print("Jan ", year, " has ", days, " days")
elif nMonth == 2 :
    print("Feb ", year, " has ", days, " days")
elif nMonth == 3 :
    print("Mar ", year, " has ", days, " days")
elif nMonth == 4 :
    print("Apr ", year, " has ", days, " days")
elif nMonth == 5 :
    print("May ", year, " has ", days, " days")
elif nMonth == 6 :
    print("Jun ", year, " has ", days, " days")
elif nMonth == 7 :
    print("Jul ", year, " has ", days, " days")
elif nMonth == 8 :
    print("Aug ", year, " has ", days, " days")
elif nMonth == 9 :
    print("Sep ", year, " has ", days, " days")
elif nMonth == 10 :
    print("Oct ", year, " has ", days, " days")
elif nMonth == 11 :
    print("Nov ", year, " has ", days, " days")
elif nMonth == 12 :
    print("Dec ", year, " has ", days, " days")
