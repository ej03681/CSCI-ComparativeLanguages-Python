y = int(input("Enter a year: "))
m = int(input("Enter a month in the year (e.g., 1 for Jan): "))
q = int(input("Enter the day of the month: 1-31: "))
    
if m == 1 :
    m = 13
    y -= 1
if m == 2 :
    m = 14
    y -= 1
    
j = y // 100
k = y % 100
    
h = (q + (26 * (m + 1) // 10) + k + (k // 4) + (j // 4) + 5 * j) % 7;

if h == 0:
    print("Day of the week is Saturday")
elif h == 1:
    print("Day of the week is Sunday")
elif h == 2:
    print("Day of the week is Monday")
elif h == 3:
    print("Day of the week is Tuesday")
elif h == 4:
    print("Day of the week is Wednesday")
elif h == 5:
    print("Day of the week is Thursday")
elif h == 6:
    print("Day of the week is Friday")