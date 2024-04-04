# Tic Tac Toe

# The game board
board = [' ' for _ in range(9)]

# Function to draw the game board
def draw_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print(row1)
    print(row2)
    print(row3)

# Function to handle player move
def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2

    print("Your turn player {}".format(number))

    while True:
        try:
            choice = int(input("Enter your move (1-9): ").strip())
            if choice < 1 or choice > 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            if board[choice - 1] != ' ':
                print("That space is taken!")
                continue
            board[choice - 1] = icon
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to check for a win
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

# Function to check for a draw
def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

# Main game loop
while True:
    draw_board()
    player_move('X')
    draw_board()
    if is_victory('X'):
        draw_board()  # Display the final state of the board
        print("Player 1 Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw!")
        break
    player_move('O')
    if is_victory('O'):
        draw_board()  # Display the final state of the board
        print("Player 2 Wins! Congratulations!")
        break