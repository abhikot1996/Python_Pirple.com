"""
Add And Remove Values into Dictionaries
"""

ThingsList = {}
def AddThingsInList():
    while True:
        TakeThings=input("Enter things which you want to add in List: ")
        if TakeThings in ThingsList:
            # if TakeThings !="Want to remove things":
                ThingsList[TakeThings]+=1
                print(ThingsList)
        else:
            if TakeThings != "-":
                ThingsList[TakeThings]=1
                print(ThingsList)
        if TakeThings == "-":
            RemoveThingsFromList()
    print(ThingsList,"\n")

def RemoveThingsFromList():
    while True:
        GiveThing=input("Enter Thing which you want to remove thing: ")
        if GiveThing in ThingsList:
            if ThingsList[GiveThing] > 0:
                ThingsList[GiveThing]-=1
                print(ThingsList)
            else: 
                print(f"{GiveThing} is over")
                print(ThingsList)
        else:
            if GiveThing !="+":
                 print(f"You don't have have {GiveThing} ")
                 print(ThingsList)
        if GiveThing == "+":
            AddThingsInList()
        # print(ThingsList)
    print(ThingsList)

AddThingsInList()
