
def password():

    print("Please enter a valid password")
    print()
    print("Your password must be between 5 and 15 characters and contain:")
    print("1 or more uppercase characters")
    print("1 or more lowercase characters")
    print("1 or more numbers")
    print("and 1 or more special characters: !@#$%^&*()_-=+`~,./o'{}\<>?O{}|")

    password = input("Please enter a password: ")

# Calculating the length of the password
    if len(password) < 5:
        return ("Password is too short")

    elif len(password)> 15:
        return("Password is too long")

    elif len(password) >= 5 and len(password) <= 15:
        return("Your password is valid")

    print(len(password))

