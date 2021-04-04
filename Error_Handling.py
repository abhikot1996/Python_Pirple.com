
keyWord = "Hello"
# print(int(keyWord))
try:
    print(int(keyWord))
# except ValueError:
#     print("Got a ValueError")
except Exception as e:
    print("Other type of exception")
    print(str(e))

finally:
    print("finally")


print("Past excetion")
