# import os
# from os import path
#
# def main():
#     # Print the name of the OS
#     print(os.name)
# #Check for item existence and type
# print("Item exists:" + str(path.exists("abhi.txt")))
# print("Item is a file: " + str(path.isfile("Participant Data.txt")))
# print("Item is a directory: " + str(path.isdir("Participant Data.txt")))
#
# if __name__ == "__main__":
#     main()

import pathlib
file = pathlib.Path("abhi.py")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")