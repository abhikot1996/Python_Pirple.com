

class Pet:
    def __init__(self,name,a,h,p): # Initialisation of variable to attributes using __init__(self)
        self.name = name
        self.age = a
        self.hunger = h
        self.playeful = p

    # getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playeful

    # setters
    def setName(self,xname):
        self.name = xname

    def setAge(self,Age):
        self.age = Age

    def setHunger(self,hunger):
        self.hunger = hunger

    def setPlayful(self,play):
        self.playful = play

    def __str__(self):
        return (self.name + " is " + str(self.age) + " years old")


class Dog(Pet):
    def __init__(self,name,age,hunger,playful,breed,FavoriteToy):
        Pet.__init__(self,name,age,hunger,playful)
        self.playful = playful
        self.breed = breed
        self.FavoriteToy = FavoriteToy
    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with "+self.FavoriteToy)
        else:
            return ("Dog doesn't want to play")

class Cat(Pet):
    def __init__(self,name,age,hunger,playful,place):
        Pet.__init__(self,name,age,hunger,playful)
        self.playful = playful
        self.FavoritePlaceToSit = place
    def wantsToSit(self):
        if self.playful == False:
            print("The cat wants to sit in",self.FavoritePlaceToSit)
        else:
            print("The cat wants to play")
    def __str__(self):
        return (self.name + " likes to sit in "+self.FavoritePlaceToSit)


huskyDog = Dog("Snowball",5,False,True,"Husky","Stick")
Play = huskyDog.wantsToPlay()
print(Play)

huskyDog.playful = False
Play = huskyDog.wantsToPlay()
print(Play)

typicalCat = Cat("Fluffy",3,False,False,"the sun ray")
typicalCat.wantsToSit()

print(typicalCat)




# Pet1 = Pet("Jim",3,False,True)
#
# print(Pet1.getName())
# print(Pet1.getPlayful())
# Pet1.setName("Snowball") # Setting name of pet
# print(Pet1.getName()) # Getting name of pet
