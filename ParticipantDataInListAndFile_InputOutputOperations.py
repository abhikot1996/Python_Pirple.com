#
# ParticipantData = []
# ParticipantNumber=2
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

Age = {}
for part in inputList:
    tempAge = int(part[-1])
    if tempAge in Age:
        Age[tempAge] +=1
    else:
        Age[tempAge]=1
print(Age)
inputFile.close()