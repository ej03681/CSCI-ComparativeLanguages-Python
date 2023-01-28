def isMarkovMatrix(m):
    sum = 0
    n = 0
    isMarkov = True
    while n < 3:
        for column in range(len(m)):
            sum = 0
            for row in range(len(m)):
                sum += m[row][column]
                
        if sum != 1:
            isMarkov = False
        n += 1
                    
    return isMarkov
    
    
def main():
    matrix = []
    for row in range(3):
        s = [float(x) for x in input("Enter a 3-3 matrix row : ").split()]
        matrix.append([])
        for column in range(3):
            matrix[row].append(s[column])
    
    if isMarkovMatrix(matrix) :
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")
main()