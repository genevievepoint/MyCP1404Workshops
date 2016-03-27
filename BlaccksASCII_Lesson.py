LOWER_VALUE = 31
UPPER_VALUE = 176
# print("Enter a number (" + {} + "-" + {} + "):".format(lower, upper))
# strip()


def get_number(lower_value, upper_value):

    lower_value = input("Enter the starting ASCII value: ").strip()

    while lower_value.isdecimal() == False:
        print("Please enter a decimal number")
        lower_value = input("Enter the starting ASCII value: ").strip()
    while lower_value < LOWER_VALUE:
        print("The lowest possible value is 10")
        lower_value = input("Please enter an ASCII value: ").strip()
    print("Thank You")

    upper_value = input("Enter the final ASCII value: ").strip()

    while upper_value.isdecimal() == False:
        print("Please enter")
        upper_value = int(input("Please enter an ASCII value: ").strip())
    while upper_value < UPPER_VALUE:
        print("The highest possible value is 50")
        upper_value = int(input("Please enter an ASCII value: ").strip())
    print("Thank You")

    integer_lower_value = int(lower_value)
    integer_upper_value = int(upper_value)

    return (integer_lower_value, integer_upper_value)

ASCII_values = get_number(LOWER_VALUE,UPPER_VALUE)

print("Displaying ASCII Value between \n (()-()) :".format(ASCII_values(0), ASCII_values(1)))

# for i in range(10, 120, 11):
#     make sure we have integers of different 'length'
#     print("{} {}".format(i, chr(i)))



