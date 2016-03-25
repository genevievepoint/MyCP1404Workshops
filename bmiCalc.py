print('Body-mass-index calculator, By Genevieve')

weight = float(input('Please enter your weight in kgs: '))
height = float(input('Please enter your height in m: '))

bmiValue = weight / (height ** 2)

print('Therefore, your BMI value is: ', bmiValue)
print('Thank you!')
