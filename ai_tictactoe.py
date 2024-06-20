import random

def is_winner(board, player):
    """
    Check if the given player has won the game.

    Parameters:
    board (list): The current state of the game board.
    player (str): The player symbol ('X' or 'O').

    Returns:
    bool: True if the player has won, False otherwise.
    """
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    """
    Check if the board is full.

    Parameters:
    board (list): The current state of the game board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

def minimax(board, depth, is_maximizing, alpha, beta):
    """
    Minimax algorithm with alpha-beta pruning to determine the best move.

    Parameters:
    board (list): The current state of the game board.
    depth (int): The current depth of the recursion.
    is_maximizing (bool): True if the current layer is maximizing, False if minimizing.
    alpha (float): The alpha value for alpha-beta pruning.
    beta (float): The beta value for alpha-beta pruning.

    Returns:
    int: The evaluation value of the board.
    """
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    """
    Determine the best move for the AI using the minimax algorithm.

    Parameters:
    board (list): The current state of the game board.

    Returns:
    tuple: The coordinates (row, col) of the best move.
    """
    best_val = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = " "
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

def easy_move(board):
    """
    Determine a random move for the AI.

    Parameters:
    board (list): The current state of the game board.

    Returns:
    tuple: The coordinates (row, col) of the move.
    """
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def medium_move(board):
    """
    Determine a medium-level move for the AI using a simple strategy.

    Parameters:
    board (list): The current state of the game board.

    Returns:
    tuple: The coordinates (row, col) of the move.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if is_winner(board, "O"):
                    return (i, j)
                board[i][j] = " "
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if is_winner(board, "X"):
                    board[i][j] = " "
                    return (i, j)
                board[i][j] = " "
    return easy_move(board)
