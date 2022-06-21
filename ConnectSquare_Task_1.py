def add_coin(board, coin, column):
    """
    This function simulates the dropping of a coin of (coin) colour into a grid, where each coordinate could be filled
    by either a clear space "0", a yellow coin "Y" or a red coin "R". The grid is represented by a list of same-length
    lists, each representing a row of spaces (and thus with a value of "0", "Y" or "R".)

    When called, the function replaces all of (column)'s empty spaces ("0") with (coin), counting each time it does
    so. Once it has completed this task, if the total coins placed is > 1, it iterates through the column
    (board[wrong_coin_row][column]) for the number of coins placed (-1 to prevent it emptying the bottom row) and
    replaces that space with a "0", since the coin would have fallen through to the space below.

    :param board: A list of even-length lists, representing rows of the board.
    :param coin: "R" or "Y", the colour of the dropped coin.
    :param column: The column (0 indexed) the coin is dropped in.
    :return: Returns the list of lists that represents the new, post-coin board state.
    """
    coins_placed = 0
    x = len(board)
    for line in board:
        if line[column] == 0:
            line[column] = coin
            coins_placed += 1
    if coins_placed == 1:
        pass
    else:
        for wrong_coin_row in range(int(coins_placed) - 1):
            board[wrong_coin_row][column] = 0
    for line in board: #currently printing w/in function because it outputs line by line, which looks nicer.
        print(line)
    return(board)

add_coin([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], 'R', 2)
print("""
-------------------
And now... for game #2:
-------------------
""")
add_coin([[0,0,0,0,0],[0,0,0,0,0],['R',0,0,0,0],['Y','R',0,'R','Y']], 'Y', 1)
