import random

MAX_INCREASE = 0.175 #17.5%
MAX_DECREASE = 0.05 #5%
MIN_PRICE = 1.00
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
INITIAL_DAY = 0

day = INITIAL_DAY
price = INITIAL_PRICE

print("Starting price: " "${:,.2f}".format(price, ".2f"))

while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) ==1:
        #generate a random floating-point number
        # between negative MAX_INCREASE and 0
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random flo floating-point number
        # between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + priceChange)

    #Creates a counter to show how many days have been simulated
    day += 1
    print("On Day {} price is: ${:,.2f}".format(day, price))