def moves_exist(board):
    """
    A move can still be made if any blank space exists on the top row
    """
    if 0 in board[0]:
        return True
    return False


def nice_print(board):
    """
    Formats the board for nicer display
    """
    for line in board:
        print(*line)


def play_game(rows, cols):
    """
    Plays a game with a human player against your AI
    """
    # Instantiate an empty board
    board = [([0] * cols) for i in range(rows)]

    # Continue playing as long as a legal move can still be made
    while (moves_exist(board)):

        # AI plays first with the red tokens
        board = ai_move(board, 'R')
        nice_print(board)

        # Check if the AI Player has won the game
        if (is_winner(board, 'R')):
            print('AI Wins!')
            break

        # Player moves next with the yellow tokens
        player_move = input('Enter your move: ')
        board = add_coin(board, 'Y', int(player_move))
        if (is_winner(board, 'Y')):
            print('You win!')
            break