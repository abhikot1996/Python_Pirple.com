import os
import pathlib

def AddFile():
    FileNameAdd = input("Enter File name: ")
    AddFile = open(FileNameAdd, "w")
    print(AddFile, " is added in Folder")
    Whichtext = input("Enter text which want to Add: ")
    AddFile.write(Whichtext)
    print("Text is added in ", AddFile)
    AddFile.close()

def ReadFile():
    RFileName = open(FileName, "r")
    for lines in RFileName:
        print(lines, end="")
    RFileName.close()

def Delete_StartOver():
    os.remove(FileName)
    print(FileName, " is Deleted")
    NewFile = open(FileName, "w")
    print(FileName," is Created")
    NewFile.close()

def Append():
    Whichtext = input("Enter text which want to Add: ")
    Addtext = open(FileName, "a")
    Addtext.write("\n")
    Addtext.write(Whichtext)
    Addtext.close()


while True:
    FileName = input("\n Enter file name or E to exit: ")
    file = pathlib.Path(FileName)
    if file.exists():

        print("A. Read file", end="\n")
        print("B. Delete file and start over", end="\n")
        print("C. Add text in file", end="\n")
        print("E. Exit")
        option = input("Choose the option: ")
        if option == "A": # To Read file
            ReadFile()
        elif option == "B": # To Delete file
            Delete_StartOver()
        elif option == "C": # To Append file
            Append()
        elif option == "E":
            break
        else:
            print("Choose A, B or C ")

    elif FileName == "E":
        break

    else:
        print("File not exist")
        WantToAdd = input(print("Want to add other file", end="\n"))
        if WantToAdd == "Yes":
            AddFile()
        elif WantToAdd == "No": # it should go to the options to enter file name
            ChooseOption()
        # else:
        #     print("Choose Yes or Not") # after it should ask again want to add file name

        #     break

