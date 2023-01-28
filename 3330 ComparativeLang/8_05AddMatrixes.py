def addMatrix(a, b):
    addM = []
    sum = 0
    for i in range(len(a[0])):
        addM.append([])
        for j in range(len(a)):
            sum = a[i][j] + b[i][j]
            addM[i].append(sum)
    return addM

def main():
    s1 = [float(x) for x in input("Enter a 3x3 matrix1: ").split()]
    s2 = [float(x) for x in input("Enter a 3x3 matrix2: ").split()]
    x1 = []
    x2 = []

    n = 0
    while n < 9:
        for i in range(3):
            x1.append([])
            x2.append([])
            for j in range(3):
                x1[i].append(s1[n])
                x2[i].append(s2[n])
                n += 1

    print(addMatrix(x1, x2))

main()

