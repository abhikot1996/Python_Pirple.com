
from random import  randint, uniform # importing specific functions from library
import random as r
randInt = randint(0,10)
print(randInt)

randUniform = uniform(1,1100)
print(randUniform)

simpleList = [1,3,5,7,11]
pickElement = r.choice(simpleList) # printing random no from list
print(pickElement)

print(simpleList)
r.shuffle(simpleList) # to shuffle list
print(simpleList)