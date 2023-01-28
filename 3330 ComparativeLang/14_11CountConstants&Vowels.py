statement = input("Enter a text: ")
statement.lower()
vowels = 0
consonants = 0

for i in range(len(statement)):
    if statement[i] == "a" or statement[i] == "e" or statement[i] == "i" or statement[i] == "o" or statement[i] == "u":
        vowels += 1
    elif statement[i] == " ":
        vowels += 0
    else :
        consonants += 1
        
print("The number of vowels is ", vowels, " and consonants ", consonants)