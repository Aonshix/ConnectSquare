# def is_winner(board, coin): """ This function searches for winning squares (a 2x2 square of spaces containing just # a single colour of coin), returning True if this is the case for the colour of (coin) or False if there is no such valid square. This is actually quite close to working, I just have to figure out how to get the loop to only operate within the right index. """
def check_for_two(board, coin):
    found_horizontals = {
        -1: [0,0]
    }
    row_count = -1
    rows = len(board)
    # print(f"The board has {rows} rows")
    row_columns = len(board[0])
    # print(f" Row columns = {row_columns}")
    # print(f"The user's coin is {coin}")
    for x in range(rows):
        found_horizontals[x] = [""]
    for row in board:
        row_count += 1
        # print(f"Increased row count to: {row_count}")
        # print(board[row_count])
        column = -1
        short_row_length = row_columns - 1
        for value in row:
            # print(f"Value = {value}")
            column += 1
            if column == short_row_length:
                    break
            # print(f"Column = {column}")
            if value == coin and row[column + 1] == coin:
                # print(f"Function has detected {value} and {row[column + 1]} are a match!")
                # print(f"Horizontal pair found: {column} and {column+1} in row {row_count}")
                found_horizontals[row_count] = [column, (column + 1)]
                # print(found_horizontals)
                if found_horizontals[row_count -1] == [column, (column+1)]:
                    return True

            else:
                # column += 1
                # print(f"Column = {column}")
                pass


        if found_horizontals[row_count] != [""]:
            pass
        else:
            found_horizontals[row_count] = [""]
        # print("Reset Column")
    return False

print(check_for_two([[0,0,0,"R","R"],[0,0,0,"R","R"],['R',0,0,0,0],['Y','R',0,'R','Y']], 'R'))



print("""

CHECKING SECOND BOARD

""")
print(check_for_two([[0,0,0,0,0],[0,0,0,0,0],['R',0,0,0,0],['Y','R',0,'R','Y']], 'Y'))


print("""

CHECKING Third BOARD

""")

print(check_for_two([['Y',0,0,0],['Y',0,0,0],['Y',0,'R','R'],['Y',0,'R','R']], 'R'))



