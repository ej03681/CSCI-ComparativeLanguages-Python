def sumColumn(m, columnIndex):
    total = 0
    for column in range(columnIndex):
        total = 0
        for row in range(len(m)):
            total += m[row][column]
    return total
    
    
def main():
    matrix = []
    
    for row in range(3):
        s = [float(x) for x in input("Enter a 3-4 matrix row :").split()]
        matrix.append([])
        for column in range(4):
            matrix[row].append(s[column])
    
    for i in range(len(matrix[0])):
        print("Sum of the elements for column ", i, " is ", sumColumn(matrix, i))
    print(matrix[0][0])
main()