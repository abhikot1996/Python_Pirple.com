#
# ParticipantData = []
# ParticipantNumber=5
# RegisteredParticipant=0
# OutputFile=open("Participant Data.txt","w")
# while RegisteredParticipant < ParticipantNumber:
#     temppartlist = []
#     name = input("Enter participant name: ")
#     temppartlist.append(name)
#     country = input("Enter participant country: ")
#     temppartlist.append(country)
#     age = int(input("Enter participant age: "))
#     temppartlist.append(age)
#     RegisteredParticipant+=1
#     print(temppartlist)
#     ParticipantData.append(temppartlist)
#     print(ParticipantData)
#
# # Adding data in file
# for participant in ParticipantData:
#     for data in participant:
#         OutputFile.write(str(data))
#         OutputFile.write(" ")
#     OutputFile.write("\n")
# OutputFile.close()

# Reading Data from file
inputFile = open("Participant Data.txt","r")
inputList = []
for line in inputFile:
    temParticipant=line.strip("\n").split()
    print(temParticipant)
    inputList.append(temParticipant)
    print(inputList)
    #  "strip()" is used to remove something from file (strip("\n")) then new line will be removed
    #  "split()" is used to split elements using space
inputFile.close()

# To find how much element has same as age
Age = {}
for part in inputList:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] +=1
    else:
        Age[tempAge]=1
print(Age)

# To find how much element has same as country
Countries = {}
for part in inputList:
    tempCountry = part[1]
    if tempCountry in Countries:
        Countries[tempCountry] +=1
    else:
        Countries[tempCountry]=1
print("Countries that attended:",Countries)

inputFile.close()

# To find oldest and Youngest age
YoungestAge = 100
Oldest = 0
mostOccuringAge = 0
counter = 0
for tempAge in Age:
    if tempAge>Oldest: # to find oldest age
        Oldest=tempAge
    if tempAge < YoungestAge: # to find youngest age
        YoungestAge=tempAge
    if Age[tempAge]>=counter: # to find most Occuring age( to find which age is repeated most times)
        counter = Age[tempAge]
        mostOccuringAge = tempAge
print("Youngest age is: ", YoungestAge)
print("Oldest age is: ", Oldest)
print("Most occuring age is:",mostOccuringAge,"wiht",counter,"participant")
inputFile.close()

