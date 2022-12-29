# move: 4
# coordinates: (1,2)
# player: {name: 'Barb', symbol: 'X'}

def move_to_coordinates(move):
    move = int(move)
    return (2 - int((move - 1) / 3), (move + 2) % 3)

def value_at_move(board, move):
    coordinates = move_to_coordinates(move)
    return board[coordinates[0]][coordinates[1]]

def check_for_win(board):
    for index in [0,1,2]:
        # check rows
        if len(set(board[index])) == 1:
            return True
        # check columns
        column_vals = [row[index] for row in board]
        if len(set(column_vals)) == 1:
            return True
    # check diagonals
    if len(set([board[0][0], board[1][1], board[2][2]])) == 1:
        return True
    elif len(set([board[0][2], board[1][1], board[2][0]])) == 1:
        return True
    return False

def is_legal_move(board, move):
    # check for value 1-9
    try:
        move = int(move)
    except ValueError:
        print("ERROR: Value must be an integer")
        return False
    if not move in range(1,10):
        print("ERROR: Value must be in range 1-9")
        return False
    # check for empty space on board
    if not type(value_at_move(board, move)) == int:
        print("ERROR: That spot is taken!")
        return False
    return True

def print_board(board):
    print()
    for index, row in enumerate(board):
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if index != 2:
            print("-----------")
    print()

def take_turn(board, player):
    print_board(board)
    print(f"{player['name']}'s turn! Enter your move: ")
    move = input()
    while not is_legal_move(board, move):
        move = input()
    coordinates = move_to_coordinates(move)
    board[coordinates[0]][coordinates[1]] = player['symbol']

def set_player(num, taken_symbols={}):
    print(f"Player {num}, please enter your name: ")
    player = {'name': input()}
    print("What symbol do you want?")
    symbol = input()
    while symbol in taken_symbols or len(symbol) != 1:
        print("ERROR: Not a valid choice. Please choose a single character that is not taken: ")
        symbol = input()
    player['symbol'] = symbol
    return player

def play_game():
    board = [[7,8,9],
                [4,5,6],
                [1,2,3]]
    player1 = set_player(1)
    player2 = set_player(2, {player1['symbol']})
    game_over = False
    while not game_over:
        take_turn(board, player1)
        if check_for_win(board): 
            print_board(board)
            print(f"{player1['name']} wins!")
            break
        take_turn(board, player2)
        if check_for_win(board): 
            print_board(board)
            print(f"{player2['name']} wins!")
            break

play_game()