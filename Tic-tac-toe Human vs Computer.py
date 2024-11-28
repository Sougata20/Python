import random

board = [' ' for _ in range(9)]
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if ' ' not in board:
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def ai_move():
    best_move = -1
    best_value = float('-inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_value = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = i
    return best_move

def player_move():
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Invalid move! Try again.")
        player_move()

def play_game():
    while True:
        print_board()
        player_move()
        if check_winner('X'):
            print_board()
            print("Player (X) wins!")
            break
        if ' ' not in board:
            print_board()
            print("It's a draw!")
            break
        print("AI is making its move...")
        move = ai_move()
        board[move] = 'O'
        if check_winner('O'):
            print_board()
            print("AI (O) wins!")
            break
        if ' ' not in board:
            print_board()
            print("It's a draw!")
            break

play_game()
