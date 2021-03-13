
import pathlib
file = pathlib.Path("abhi.txt")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")