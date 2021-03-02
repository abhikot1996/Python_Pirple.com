

def isnumsame(a,b,c):
    if a==b or a==c or b==c:
        return True
    else:
        return False
print("Enter Three numbers: ")
d,e,f = int(input()), int(input()),int(input())
callisnumsame = isnumsame(d,e,f)
print(callisnumsame)
# print(isnumsame(d,e,f))