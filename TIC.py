def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def play_game():
    board = "123456789"
    current_player = 'X'
    
    print("Welcome to String-Based Tic-Tac-Toe!")
    print_board(board)
    
    for turn in range(9):
        while True:
            choice = input(f"Player {current_player}, choose a position (1-9): ").strip()
            
            if choice not in board or choice in ['X', 'O']:
                print("Invalid move or position already taken. Try again.")
                continue
                
            index = board.index(choice)
            break
            
        board = board[:index] + current_player + board[index+1:]
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins! 🎉")
            return
            
    print("It's a draw! 🤝")

if '_name_' == "_main_":
    play_game()
