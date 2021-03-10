def TicTacToe(CurrentPosition):
    for row in range(1,6):
        for column in range(1,6):
            if row%2:
                if column%2==0:
                    print("|",end="")
                else:
                        print(CurrentPosition[row//2][column//2],end="")
            else:
                print("-",end="")
        print(end="\n")

CurrentPosition=[[" "," "," "], [" "," "," "], [" "," "," "],]
# print(CurrentPosition)
TicTacToe(CurrentPosition)
Player = 1
while True:
    if CurrentPosition[0][0] == CurrentPosition[0][1] == CurrentPosition[0][2] and CurrentPosition[0][0] != " " and CurrentPosition[0][1] != " " and CurrentPosition[0][2] != " ":
        if CurrentPosition[0][0]=="X" and CurrentPosition[0][1] == "X" and CurrentPosition[0][2] == "X" :
            print("Player 1 won the game" )
        elif CurrentPosition[0][0]=="O" and CurrentPosition[0][1] == "O" and CurrentPosition[0][2] == "O" :
            print("Player 2 won the game")
        break

    elif CurrentPosition[1][0] == CurrentPosition[1][1] == CurrentPosition[1][2] and CurrentPosition[1][0] != " " and CurrentPosition[1][1] != " " and CurrentPosition[1][2] != " ":
        if CurrentPosition[1][0] == "X" and CurrentPosition[1][1] == "X" and CurrentPosition[1][2] == "X":
            print("Player 1 won the game")
        elif CurrentPosition[1][0] == "O" and CurrentPosition[1][1] == "O" and CurrentPosition[1][2] == "O":
            print("Player 2 won the game")
        break

    elif CurrentPosition[2][0] == CurrentPosition[2][1] == CurrentPosition[2][2] and CurrentPosition[2][0] != " " and CurrentPosition[2][1] != " " and CurrentPosition[2][2] != " ":
        if CurrentPosition[2][0] == "X" and CurrentPosition[2][1] == "X" and CurrentPosition[2][2] == "X":
            print("Player 1 won the game")
        elif CurrentPosition[2][0] == "O" and CurrentPosition[2][1] == "O" and CurrentPosition[2][2] == "O":
            print("Player 2 won the game")
        break

    elif CurrentPosition[0][0] == CurrentPosition[1][0] == CurrentPosition[2][0] and CurrentPosition[0][0] != " " and CurrentPosition[1][0] != " " and CurrentPosition[2][0] != " ":
        if CurrentPosition[0][0] == "X" and CurrentPosition[1][0] == "X" and CurrentPosition[2][0] == "X":
            print("Player 1 won the game")
        elif CurrentPosition[0][0] == "O" and CurrentPosition[1][0] == "O" and CurrentPosition[2][0] == "O":
            print("Player 2 won the game")
        break

    elif CurrentPosition[0][1] == CurrentPosition[1][1] == CurrentPosition[2][1] and CurrentPosition[0][1] != " " and CurrentPosition[1][1] != " " and CurrentPosition[2][1] != " ":
        if CurrentPosition[0][1] == "X" and CurrentPosition[1][1] == "X" and CurrentPosition[2][1] == "X":
            print("Player 1 won the game")
        elif CurrentPosition[0][1] == "O" and CurrentPosition[1][1] == "O" and CurrentPosition[2][1] == "O":
            print("Player 2 won the game")
        break

    elif CurrentPosition[0][2] == CurrentPosition[1][2] == CurrentPosition[2][2] and CurrentPosition[2][2] != " " and CurrentPosition[0][2] != " " and CurrentPosition[1][2] != " ":
        if CurrentPosition[0][2] == "X" and CurrentPosition[1][2] == "X" and CurrentPosition[2][2] == "X":
            print("Player 1 won the game")
        elif CurrentPosition[0][2] == "O" and CurrentPosition[1][2] == "O" and CurrentPosition[2][2] == "O":
            print("Player 2 won the game")
        break

    elif CurrentPosition[0][0] == CurrentPosition[1][1] == CurrentPosition[2][2] and CurrentPosition[0][0] != " " and CurrentPosition[1][1] != " " and CurrentPosition[2][2] != " ":
        if CurrentPosition[0][0] == "X" and CurrentPosition[1][1] == "X" and CurrentPosition[2][2] == "X":
            print("Player 1 won the game")
        elif CurrentPosition[0][0] == "O" and CurrentPosition[1][1] == "O" and CurrentPosition[2][2] == "O":
            print("Player 2 won the game")
        break

    elif CurrentPosition[0][2] == CurrentPosition[1][1] == CurrentPosition[2][0] and CurrentPosition[0][2] != " " and CurrentPosition[1][1] != " " and CurrentPosition[2][0] != " ":
        if CurrentPosition[0][2] == "X" and CurrentPosition[1][1] == "X" and CurrentPosition[2][0] == "X":
            print("Player 1 won the game")
        elif CurrentPosition[0][2] == "O" and CurrentPosition[1][1] == "O" and CurrentPosition[2][0] == "O":
            print("Player 2 won the game")
        break

    elif CurrentPosition[0][0]!=" " and CurrentPosition[0][1]!=" " and CurrentPosition[0][2]!=" "and CurrentPosition[1][0] != " " and CurrentPosition[1][1] != " " and CurrentPosition[1][2] != " " and CurrentPosition[2][0] != " " and CurrentPosition[2][1] != " " and CurrentPosition[2][2] != " ":
        print("Draw")
        break

    else:
        print("Player: ",Player)
        MoveRow = int(input("Enter row number: "))
        MoveColumn = int(input("Enter column number: "))
        if Player==1:
            if CurrentPosition[MoveRow][MoveColumn] == " ":
                CurrentPosition[MoveRow][MoveColumn] = "X"
                Player=2
                # print(CurrentPosition)
                TicTacToe(CurrentPosition)
        else:
            if CurrentPosition[MoveRow][MoveColumn] == " ":
                CurrentPosition[MoveRow][MoveColumn] = "O"
                Player=1
                # print(CurrentPosition)
                TicTacToe(CurrentPosition)

# Draw Game
# O|X|X
# -----
# X|O|O
# -----
# X|O|X