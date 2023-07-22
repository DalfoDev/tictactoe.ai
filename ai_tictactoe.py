import random

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

def is_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([board[i][j] != " " for i in range(3) for j in range(3)])

def get_valid_input():
    while True:
        try:
            user_input = int(input("Enter a number between 1 and 9: "))
            if 1 <= user_input <= 9:
                return user_input
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def ai_move_easy(board):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_positions)

def ai_move_medium(board, player):
    # Check if AI can win in the next move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if is_winner(board, player):
                    return i, j
                board[i][j] = " "

    # Check if the player can win in the next move and block them
    opponent = "X" if player == "O" else "O"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = opponent
                if is_winner(board, opponent):
                    return i, j
                board[i][j] = " "

    # If no winning move or blocking move, make a random move
    return ai_move_easy(board)

def ai_move_hard(board, player):
    best_score = float("-inf")
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def ai_move_impossible(board, player):
    best_score = float("-inf")
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                score = alphabeta(board, 0, False, float("-inf"), float("inf"))
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def minimax(board, depth, is_maximizing):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def alphabeta(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = alphabeta(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = alphabeta(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    player_idx = random.randint(0, 1)  # Randomly determine who goes first
    difficulty_levels = {1: ai_move_easy, 2: ai_move_medium, 3: ai_move_hard, 4: ai_move_impossible}
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    print("Choose the difficulty level:")
    print("1 - Easy")
    print("2 - Medium")
    print("3 - Hard")
    print("4 - Impossible")
    
    while True:
        try:
            chosen_level = int(input("Enter the number corresponding to the difficulty level: "))
            if chosen_level in difficulty_levels:
                difficulty_level = difficulty_levels[chosen_level]
                break
            else:
                print("Invalid input. Please choose 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please choose 1, 2, 3, or 4.")

    for _ in range(9):
        if player_idx == 0:  # AI's turn
            if callable(difficulty_level):
                ai_row, ai_col = difficulty_level(board, players[player_idx])
            else:
                print("Invalid difficulty level. Please choose from 1, 2, 3, or 4.")
                return

            board[ai_row][ai_col] = players[player_idx]
            print(f"AI's turn (Player {players[player_idx]}):")
        else:  # User's turn
            print(f"Your turn (Player {players[player_idx]}):")
            valid_input = False
            while not valid_input:
                position = get_valid_input()
                row = (position - 1) // 3
                col = (position - 1) % 3
                if board[row][col] == " ":
                    board[row][col] = players[player_idx]
                    valid_input = True
                else:
                    print("Invalid move. Position already taken.")

        print_board(board)
        if is_winner(board, players[player_idx]):
            print(f"Player {players[player_idx]} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        player_idx = (player_idx + 1) % 2

if __name__ == "__main__":
    play_game()