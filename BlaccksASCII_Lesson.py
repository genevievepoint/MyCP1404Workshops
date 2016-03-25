# lower = 10
# upper = 100
# print("Enter a number (" + {} + "-" + {} + "):".format(lower, upper))
#strip()

lower_value = int(input("Please enter an ASCII value: ").strip())
while lower_value < 10 and lower_value >50:
   print("The lowest possible value is 10")
   lower_value = int(input("Please enter an ASCII value: ").strip())
print("Thank You")

upper_value = int(input("Please enter an ASCII value: ").strip())
while upper_value <10 and upper_value >50:
   print("The highest possible value is 50")
   upper_value = int(input("Please enter an ASCII value: ").strip())
print("Thank You")

for i in range(10, 120, 11):
    # make sure we have integers of different 'length'
    print("{} {}".format(i, chr(i)))

def get_number(lower_value, upper_value):
    
