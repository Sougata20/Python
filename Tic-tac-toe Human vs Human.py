board = [' ' for _ in range(9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combo) for combo in winning_combinations)

def player_move(player):
    move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    if board[move] == ' ':
        board[move] = player
    else:
        print("Invalid move! Try again.")
        player_move(player)

def play_game():
    current_player = 'X'
    while True:
        print_board()
        player_move(current_player)
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break
        if ' ' not in board:
            print_board()
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

play_game()
