
from random import random
from time import clock
randVal = random()
print(randVal)

upper = 1.0
lower = 0.0
# guess = 0.5
startTime = clock()
while True:
    guess = (upper + lower) / 2
    if guess == randVal:
        break
    elif guess < randVal:
        lower = guess
    else:
        upper = guess

endTime = clock()
print(guess)
print("It took us:",endTime - startTime,"seconds")
