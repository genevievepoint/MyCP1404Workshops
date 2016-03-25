finished = False
result = 0
while not finished:
    try:
        result = input("Please Enter a Number: ")

    except result != int:
        print("Please enter a valid integer.")
print("valid result is", result)