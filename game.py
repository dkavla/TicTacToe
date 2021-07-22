
from logic import  *

# create players
player_1, player_2 = 'X', 'O'

# initialize board and list for holding all taken positions
game_board = create_board()
taken_positions = []

# Output Introduction and Instructions
print("\nTic Tac Toe")
print("Inorder to input you choice of position, you have \nto input both the row(1-3) and column(1-3)\n")

display_board(game_board)

current_player = player_1
spots_taken = 0


while evaluate_board_p1 or eval_board_p2:
    # check if there are any positions left to take
    if len(taken_positions) == 9:
        break

    if current_player == player_1:
        print("\nPlayer 1's turn:")
        row, col = get_input(player_1, taken_positions)
        taken_positions.append((row, col))
        game_board = update_board(player_1, row, col - 1, game_board)
        current_player = player_2
        display_board(game_board)
    else:
        print("\nPlayer 2's turn:")
        row, col = get_input(player_2,  taken_positions)
        taken_positions.append((row, col))
        game_board = update_board(player_2, row, col - 1, game_board)
        spots_taken += 1
        current_player = player_1
        display_board(game_board)
    
    if evaluate_board_p1(game_board):
        print("Player 1 wins")
        break
    elif eval_board_p2(game_board):
        print("Player 2 wins")
        break
    
if not evaluate_board_p1(game_board) and not eval_board_p2(game_board):
    print("No winners.")
print("Game Over!")









