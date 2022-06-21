# def is_winner(board, coin):
#     """
#     This function searches for winning squares (a 2x2 square of spaces containing just a single colour of coin),
#     returning True if this is the case for the colour of (coin) or False if there is no such valid square.
#     """
#     if:
#         return True
#
#     else:
#         return False
def check_for_two(board, coin):
    rows = len(board)
    print(f"The board has {rows} rows")
    row_count = -1
    print(coin)
    for row in board:
        row_count += 1
        row_length = len(row)
        print(f" Row length = {row_length}")
        column = -1
        short_row_length = row_length - 2
        while column <= short_row_length:
            for value in row:
                print(f"Value = {value}")
                if value == coin and row[column + 2] == coin:
                    column += 1
                    print(f"Column = {column}")
                    print(f"Function has detected {value} and {row[column +1]} are a match!")
                    print(f"Horizontal pair found: {column} and {column+1} in row {row_count}")
                else:
                    column += 1
                    print(f"Column = {column}")


        column = -1
        print("Reset Column")

        print(f"Increased row count to: {row_count}")


check_for_two([[0,0,'R','R',0],['R','R',0,0,0],['R',0,0,0,0],['Y','R',0,'R','Y']], 'R')

# check_for_two([['Y',0,0,0],['Y',0,0,0],['Y',0,'R','R'],['Y',0,'R','R']], 'R')



