words = input("Enter a text: ")
words = words.split()
words.sort()
    
output = []
for x in words:
    if x not in output:
        output.append(x)
        
for x in output:
    print(x, end = " ")