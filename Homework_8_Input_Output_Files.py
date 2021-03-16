import os
from os import walk
import pathlib

def AddFile(): # To Add new file
    FileNameAdd = input("Enter File name: ")
    isfilenameexist = pathlib.Path(FileNameAdd)
    if isfilenameexist.exists():
        print("File is already exist")
    else:
        AddFile = open(FileNameAdd, "w")
        print(FileNameAdd, " is added in Folder")
        Whichtext = input("Enter text which want to Add: ")
        AddFile.write(Whichtext)
        print("Text is added in ", FileNameAdd)
        AddFile.close()

def ReadFile(): # To Read file
    LineNo=0
    RFileName = open(FileName, "r")
    for lines in RFileName:
        LineNo+=1
        print(LineNo,".",lines, end="")
    RFileName.close()

def Delete_StartOver(): # To Delete and Create New file
    os.remove(FileName)
    print(FileName, " is Deleted")
    NewFile = open(FileName, "w")
    print(FileName," is Created")
    NewFile.close()

def Append(): # To Add new text in file
    Whichtext = input("Enter text which want to Add: ")
    Addtext = open(FileName, "a")
    Addtext.write("\n")
    Addtext.write(Whichtext)
    Addtext.close()

def RepalceLine(): # To Replace text in file
    if file.exists():
        ReadFile()
        OldText = input("\nEnter old text: ")
        NewText = input("Enter New text: ")
        OpenFile = open(FileName, "rt")
        data = OpenFile.read()
        data = data.replace(OldText, NewText)
        OpenFile.close()

        OpenFile = open(FileName, "wt")
        OpenFile.write(data)
        ReadFile()
        OpenFile.close()
    else:
        print("File is no exist")

while True:
    NewFile = input("""\nWant to add file, Enter 'Yes' or 'No' or 'E' to exit: """)
    while True:
        if NewFile=="Yes":
            AddFile()
            break
        elif NewFile == "No":
            filenames = next(walk("E:\AK\Study\Programming Languages\GitHub\Pirple.com\Python_Pirple.com"))
            print(filenames)
            FileName = input("\n Enter file name from above files or E to exit: ")

            while True:
                file = pathlib.Path(FileName)
                if file.exists():
                    print("\nA. Read file",end="\n")
                    print("B. Delete file and start over,",end="\n")
                    print("C. Add text in file", end="\n")
                    print("D. Replace text line in file", end="\n")
                    print("E. Exit")
                    option = input("Choose the option: ")
                    if option == "A": # To Read file
                        ReadFile()
                    elif option == "B": # To Delete file
                        Delete_StartOver()
                    elif option == "C": # To Append file
                        Append()
                    elif option == "D": # To Replace text line in file
                        RepalceLine()
                    elif option == "E":
                        break
                    else:
                        print("Choose A, B, C, D or E ")

                elif FileName == "E":
                    break
                else:
                    print("File not exist")
                    break

            if FileName == "E":
                break
        elif NewFile == "E":
            break
        else:
            print("Enter 'Yes' or 'No' or for Exit 'E'")
            break
    if NewFile == "E":
        break
