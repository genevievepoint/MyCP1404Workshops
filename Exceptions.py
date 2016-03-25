try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# 1. A ValueError will occur when anything other than an integer is entered.
# 2. A ZeroDivisionError will occur when a number is attempted to be divided by zero.
# 3. Make zero a non-valid number.
