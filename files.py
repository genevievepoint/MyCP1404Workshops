
# Program 1
outFile = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=outFile)
outFile.close()

# Program 2
in_file = open("name.txt", "r")
name = input("What is your name? ")
print("Your name is", name)
in_file.close()

# Program 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()