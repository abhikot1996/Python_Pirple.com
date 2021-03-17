

def EmptyGameBoard(ColumnNo):
    for r in range(1,7):
        for c in range(1,16):
                if c%2:
                    print("|",end="")
                else:
                    if r==5 and c==ColumnNo:
                        print("O",end="")
                    else:
                        print(" ", end="")
        print(end="\n")

def PlayerOne():
    print("X",end="")

def PlayerTwo():
    print("O",end="")

# EmptyGameBoard()

EnterColumnNo= int(input("Enter column no: "))
ColumnNo = EnterColumnNo + EnterColumnNo
EmptyGameBoard(ColumnNo)