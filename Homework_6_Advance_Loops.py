

def TicTacToe(row1,column1):
    if row1 != column1 and row1<=59 and column1<=59:
        print("Row and Column should have same value")
        return False
    elif row1<=59 and column1<=59:
        for row in range(row1 * 2):
            for column in range(1, column1 *2):
                if row % 2 == 0:
                    if column % 2:
                        print("|", end="")
                    else:
                        print(" ", end="")
                else:
                    print("-", end="")
            print(end="\n")
        if row1 == column1:
            return True
    else:
        print("Rows and Columns values should be less than or equal 59")
        return False

RowAndColumn = TicTacToe(59,59)
if RowAndColumn == True or RowAndColumn == False:
    print(RowAndColumn)



