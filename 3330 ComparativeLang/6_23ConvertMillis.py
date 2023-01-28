def convertMillis(millis):
    print(int(millis/1000/60/60), ":", int(millis/1000/60%60), ":", int(millis/1000%60))
        
def main():
    millis = float(input("Enter time in milliseconds: "))
    print(convertMillis(millis))
main()