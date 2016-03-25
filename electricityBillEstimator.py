# I cant get estimator 2 to work


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print('Electricity bill estimator')

# 11 = TARIFF_11
# 31 = TARIFF_31

pricePerKWh = float(input('Enter cents per kWh: '))
dailyUse = float(input('Enter daily use in kWh: '))
numberOfDays = float(input('Enter number of billing day: '))

totalUsage = dailyUse * numberOfDays
estimatedBill = (totalUsage * pricePerKWh) / 100

print('Estimated bill: $', estimatedBill)

print('Electricity bill estimator 2.0')

userTariff = input('Which tariff? 11 or 31: ')
dailyUse = float(input('Enter daily use in kWh: '))
numberOfDays = float(input('Enter number of billing day: '))

estimatedBill = (userTariff * dailyUse * numberOfDays) / 100

print('Estimated bill: ', estimatedBill)