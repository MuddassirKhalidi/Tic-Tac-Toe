"""
Tic Tac Toe Game
"""

import random
from tabulate import tabulate



def display_board(board):
    """
    Display the Tic Tac Toe board.
    """
    headers = ['0', '1', '2']
    table = tabulate(board, headers, tablefmt='fancy_grid', showindex=['0', '1', '2'])
    print(table)

def check_win(board, symbol):
    """
    Check if a player has won.
    """
    # Check rows
    if any(all(cell == symbol for cell in row) for row in board):
        return True

    # Check columns
    if any(all(row[col] == symbol for row in board) for col in range(len(board[0]))):
        return True

    # Check left diagonal
    if all(board[i][i] == symbol for i in range(len(board))):
        return True

    # Check right diagonal
    if all(board[i][len(board) - 1 - i] == symbol for i in range(len(board))):
        return True

    return False
class DuplicateError(Exception):
    """
    Exception raised for duplicate inputs.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Position already filled"):
        self.message = message
        super().__init__(self.message)

def validate_user_input(user_inputs):
    """
    Validate user input for the position.
    """
    while True:
        try:
            input_str = input('Enter the position where you want to input: ')
            index1, index2 = map(int, input_str.split())
            if (index1, index2) in user_inputs:
                raise DuplicateError('Position already filled')
            if index1 not in range(3) or index2 not in range(3):
                raise ValueError
        except ValueError as value_error:
            print(f'ValueError: {value_error}')
        except DuplicateError as duplicate_error:
            print(f'DuplicateError: {duplicate_error}')
        else:
            return index1, index2

def computer_play():
    """
    Play against the computer.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    valid_inputs = [(x,y) for x in range(3) for y in range(3)]
    user_inputs = set()
    for turn in range(9):
        symbol = ''
        if turn % 2 == 0:
            print('-' * 50)
            print("Computer's turn!")
            symbol = 'x'
            index1,index2 = random.choice(valid_inputs)
            board[index2][index1] = symbol
            if check_win(board, symbol):
                display_board(board)
                print('Computer WINS!')
                print('-' * 50)
                break
            display_board(board)
            valid_inputs.remove((index1,index2))
            user_inputs.add((index1,index2))
        else:
            print('-' * 50)
            print("Your turn!")
            symbol = 'o'
            index1,index2 = validate_user_input(user_inputs)
            board[index2][index1] = symbol
            if check_win(board, symbol):
                display_board(board)
                print('You WIN!')
                print('-' * 50)
                break
            display_board(board)
            valid_inputs.remove((index1,index2))
            user_inputs.add((index1,index2))
def multiplayer_game(player1, player2):
    """
    Play a multiplayer game.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    user_inputs = set()

    for turn in range(9):
        print('-' * 50)
        display_board(board)

        current_player = player1 if turn % 2 == 0 else player2
        print(f'{current_player}! Your turn')

        index1, index2 = validate_user_input(user_inputs)
        user_inputs.add((index1, index2))

        symbol = 'x' if turn % 2 == 0 else 'o'
        board[index2][index1] = symbol

        if check_win(board, symbol):
            display_board(board)
            print(f'{current_player} WINS!')
            print('-' * 50)
            break

        if turn == 8:
            display_board(board)
            print("It's a DRAW!")



# Start the game
print('WELCOME TO THE TIC TAC TOE GAME!'.center(75))
print('INSTRUCTIONS')
print('When you enter a position, enter in this format {column number} {row number}')


while True:
    try:
        print('''1. Play Against Computer (Enter 1)
2. Play Against a Friend (Enter 2)
3. Exit (Enter 3)''')
        choice = int(input())
        while choice not in [1, 2, 3]:
            choice = int(input('Enter a valid choice: '))
    except ValueError:
        print('Integer Values Only!')
    else:
        if choice == 1:
            computer_play()
            continue
        if choice == 2:
            player1_name = input('Enter the name of Player 1: ')
            player2_name = input('Enter the name of Player 2: ')
            multiplayer_game(player1_name, player2_name)
            continue
        if choice == 3:
            print('Goodbye!')
            raise SystemExit
