
Player = 1
CurrentPosition = [[" " ," ", " "], [" " ," ", " "], [" " ," ", " "]]
print(CurrentPosition)
while True:
    print("Player turn: ",Player)
    MoveRow = int(input("Please enter the row: "))
    MoveColumn = int(input("Please enter the column: "))
    if Player==1:
        CurrentPosition[MoveColumn][MoveRow]="X"
        print(CurrentPosition)
        Player=2
    else:
        CurrentPosition[MoveColumn][MoveRow]="O"
        print(CurrentPosition)
        Player=1
