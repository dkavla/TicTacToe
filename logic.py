# creates the initial board, also used for restarting
def create_board():
    board = {
        1: [1, 2, 3],
        2: [4, 5, 6],
        3: [7, 8, 9]
    }
    return board

# displays board
def display_board(board):
    for k in board.keys():
        row = board[k]
        print("---------")
        for i in range(len(row)):
            print(row[i], "|", row[i + 1], "|", row[i +2])
            break

# retrieves current player's input
def get_input(player,  taken_positions):
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))

    # evaluate the player's input
    if invalid_input(row, col):
        print("Invalid input for row and column.")
        return get_input(player,  taken_positions)
    elif ((row, col) in taken_positions):
        print("Position(s) taken.")
        print("")
        return get_input(player, taken_positions)
    else:
        return row, col

def invalid_input(row, col):
    if (row not in range(1, 4)) or (col not in range(1, 4)): 
        return True
    else:
        return False

# updates board each turn
def update_board(player, row, col, board):
    board[row][col] = player
    return board

# evaluates if player 1 won
def evaluate_board_p1(board):
    # Player 1 evaluations
    if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    elif board[1][0] == 'X' and board[2][1] == 'X' and board[3][2] == 'X':
        return True
    elif board[1][1] == 'X' and board[2][1] == 'X' and board[3][1] == 'X':
        return True
    elif board[1][2] == 'X' and board[2][2] == 'X' and board[3][2] == 'X':
        return True
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    elif board[3][0] == 'X' and board[3][1] == 'X' and board[3][2] == 'X':
        return True
    elif board[3][0] == 'X' and board[2][1] == 'X' and board[1][2] == 'X':
        return True
    else:
        return False

# evaluates if player 2 won
def eval_board_p2(board):
    # Player 2 evaluations
    if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return True
    elif board[1][0] == 'O' and board[2][1] == 'O' and board[3][2] == 'O':
        return True
    elif board[1][1] == 'O' and board[2][1] == 'O' and board[3][1] == 'O':
        return True
    elif board[1][2] == 'O' and board[2][2] == 'O' and board[3][2] == 'O':
        return True
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return True
    elif board[3][0] == 'O' and board[3][1] == 'O' and board[3][2] == 'O':
        return True
    elif board[3][0] == 'O' and board[2][1] == 'O' and board[1][2] == 'O':
        return True
    else:
        return False
