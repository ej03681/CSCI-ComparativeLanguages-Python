
def binaryToHex(binaryValue):
    for i in range(1):
        Hex = hex(int(binaryValue, 2))
        Hex = Hex[2] + Hex[3].upper()
    return Hex
def main():
    binary = input("Enter a binary number: ")
    print("The hex value is", str(binaryToHex(binary)))
main()