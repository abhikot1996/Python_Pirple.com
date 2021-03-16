#


#
# OpenFile1=open("Moral Stories.txt","r+")
# ReadFile()
# EnterLineNo=int(input("Enter line no: "))
# LineNo=0
# for lines in OpenFile1:
#     LineNo+=1
#     if EnterLineNo == LineNo:
#         OldText=lines
#         # print(lines)
#         NewText = input("Enter New text: ")
#         str(lines).replace(OldText,NewText)
#         ReadFile()
#         # lines1=lines
#         #
#         # str.strip(lines)
#         # str.replace(NewText,lines1)
#         # ReadFile()
# OpenFile1.close()



# f = open("Moral Stories.txt","rt")
# data = f.read()
# data = data.replace("100 Moral Stories 74 www.islamicoccasions.co","dofugosdfgisdfisdyfio")
# f.close()
# f=open("Moral Stories.txt","wt")
# f.write(data)
# f.close()

# OpenFile=open("Moral Stories.txt","rt")
# ReadFile=OpenFile.read()
# ReadFile = ReadFile.replace("A SENSE OF A GOOSE","sdfsdddddddddddddddddd")
# OpenFile.close()
# OpenFile = open("Moral Stories.txt","wt")
# OpenFile.write(ReadFile)
# OpenFile.close()


def ReadFile(FileName):
    OpenFile=open(FileName,"r")
    LineNo = 0
    for lines in OpenFile:
        LineNo += 1
        print(LineNo,".",lines)
    OpenFile.close()
#
# FileName=input("Enter file name: ")
# OpenFileToRead = open(FileName, "r")
# ReadFile(FileName)
# NewText = input("Enter new text: ")
# LineNo = 0
# EnterLineNo=int(input("Enter line no: "))
# new_file_content = ""
# for line in OpenFileToRead:
#     LineNo+=1
#     if EnterLineNo==LineNo:
#         # stripped_line = line.strip()
#         new_line = line.replace(line,NewText)
#         new_file_content += new_line +"\n"
# OpenFileToRead.close()
#
# OpenFileToWrite = open(FileName, "w")
# OpenFileToWrite.write(new_file_content)
# OpenFileToWrite.close()


FileName = input("Enter file name: ")
ReadFile(FileName)
# EnterLineNo=int(input("Enter line no: "))
# OldText=EnterLineNo
OldText=input("Enter old text: ")
NewText=input("Enter New text: ")
OpenFile = open(FileName, "rt")
data = OpenFile.read()
data = data.replace(OldText,NewText)

OpenFile.close()
OpenFile = open(FileName, "wt")
OpenFile.write(data)
ReadFile(FileName)
OpenFile.close()


