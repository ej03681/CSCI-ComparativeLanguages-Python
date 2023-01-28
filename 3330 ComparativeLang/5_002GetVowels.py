statement = str(input("Enter a string: "))
statement = statement.lower()
vowels = ''
for i in range(0, len(statement)):
    if statement[i] == "a" or statement[i] == "e" or statement[i] == "i" or statement[i] == "o" or statement[i] == "u":
        vowels += statement[i]
print("The vowels are ", vowels)