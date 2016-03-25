import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
INITIAL_DAY = 1

day = INITIAL_DAY + 1
print(day)

price = INITIAL_PRICE
print("$" + format(price, ".2f"))

while price >+ MIN_PRICE and price <+ MAX_PRICE:
    priceChange = 0
#        generates a random integer of 1 or 2
#           if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) ==1:
        #generate a random floating-point number
            #between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        #generate a random floating-point number
            #between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + priceChange)
    print("On Day ", day, "price is: " "$" + format(price, ".2f"))