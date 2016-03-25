print('Temperature Conversion program')

celsiusValue = float(input('Please enter a temperature is degrees celsius: '))
fahrenheitValue = celsiusValue * 9 / 5 + 32
kelvinValue = celsiusValue + 273.15

print('celsius value: ', celsiusValue)
print('fahrenheit value', fahrenheitValue)
print('kelvin value: ', kelvinValue)