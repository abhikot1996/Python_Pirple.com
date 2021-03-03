
MyUniqueList = []
MyLeftOvers  = []

def AddMyLeftOvers(element1):
    MyLeftOvers.append(element1)
    return "Added in MyLeftOvers List, it's already in MyUniqueList"


def AddMyUniqueList(element):
        if element in MyUniqueList:
            print(AddMyLeftOvers(element))
            return False
        else:
            MyUniqueList.append(element)
            print("Added in MyUnique")
            return True



print(AddMyUniqueList(1)) # True
print(MyUniqueList) # Output, 1 will be added in to list
print(AddMyUniqueList(1)) # False
# print(MyUniqueList) # Output, 1 won't be added in to list
print(MyLeftOvers) # Printing values which are added in MyLeftOvers List which values are not added in MyUniqueList
print(AddMyUniqueList(2)) # True
print(MyUniqueList) # Output, 2 will be added in to list
print(AddMyUniqueList(2.3)) # True
print(MyUniqueList)  # Output, 2.3 will be added in to list
print(AddMyUniqueList("Hello")) # True
print(MyUniqueList) # Output, "Hello" will be added in to list
print(AddMyUniqueList(2)) # False
# print(MyUniqueList) # # Output, 2 won't be added in to list
print(MyLeftOvers) # Printing values which are added in MyLeftOvers List which values are not added in MyUniqueList
print(AddMyUniqueList('Hello')) # False
# print(MyUniqueList) # Output, 'Hello' won't be added in to list
print(MyLeftOvers) # Printing values which are added in MyLeftOvers List which values are not added in MyUniqueList
print(AddMyUniqueList(1))
print(MyLeftOvers) # Printing values which are added in MyLeftOvers List which values are not added in MyUniqueList
