"""
File Input Output
"""
# VacationSpots=["London","Paris","New York","Utah","Iceland"]
# VacationFile = open("Vacation Places","w")
# "w" to write file
# e.g 1),
# for spots in VacationSpots:
#     VacationFile.write(spots +", ") # If there is only strings then use direct variable like spotes
#                                     # else converte it into string using "str()" fun.
# print("Done")
# VacationFile.close()

# "r" to Read file
# e.g 1),
# If file is small then use this "read()" function.
# VacationFile=open("Vacation Places","r")
# TheWholeFile= VacationFile.read()
# print(TheWholeFile)
# VacationFile.close()

# e.g 2),
# If file is Big then read it line by line.
# VacationFile = open("Vacation Places","r")
# for line in VacationFile:
#     print(line)
# VacationFile.close()

# e.g 3),
# To Read Line by lien
# VacationFile = open("Vacation Places","r")
# FirstLine= VacationFile.readline()
# print(FirstLine,end="")
# SecondLine= VacationFile.readline()
# print(SecondLine,end="")
# VacationFile.close()

# "a" to append text in file (To Add text into the end of the file)
# e.g 1),
# FinalSpot = "Thailand"
# VacationFile = open("Vacation place","a")
# VacationFile.write(FinalSpot)
# VacationFile.close()

# VacationFile=open("Vacation Places","r") # To read file after appending text
# for spots in VacationFile:
#     print(spots,end="")
# VacationFile.close()

# Using "with" keyword to open file
# e.g 1),
# with open ("Vacation Places","r") as VacationFile: # If file is opened in "with" Keyword format then need not to close file.
#     for spots in VacationFile:
#         print(spots,end="")

