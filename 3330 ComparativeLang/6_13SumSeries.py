def sumSeries(i):
    sum = 0
    for n in range(1, i + 1):
        sum =sum + n / (n + 1) 
    return sum 
def main():
    for i in range(21):
        if i == 0:
            print("i        m(i)")
        else:
            print(i, "      ", round(sumSeries(i), 4))
main()