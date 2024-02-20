import random
import os


'''
Initialization function for the game
'''
def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

'''
Function for adding a new tile: 90% 2-tile, 10% 4-tile
'''
def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

'''
The function that prints the board
'''
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("2048 Game:")
    for row in board:
        print(" ".join(f"{x:5}" if x != 0 else '     ' for x in row))

'''
The function that slide a row
'''
def slide(row):
    slided = False
    new_row = [i for i in row if i != 0]
    for _ in range(len(row) - len(new_row)):
        new_row.append(0)
    for i in range(len(new_row)):
        if new_row[i] != row[i]:
            slided = True
    return new_row, slided


'''
The function that merge two tiles together
'''
def merge(row):
    merged = False
    for i in range(len(row) - 1):
        if row[i] == row[i+1] and row[i] != 0:
            row[i] *= 2
            row[i+1] = 0
            merged = True
    return row, merged



'''
Moving functions
'''
def move_left(board):
    moved = False
    new_board = [[],[],[],[]]
    for i in range(len(board)):
        new_board[i], slide_occur = slide(board[i])
        moved = moved or slide_occur
    for i in range(len(new_board)):
        new_board[i], merge_coccur = merge(new_board[i])
        moved = moved or merge_coccur
    for i in range(len(new_board)):
        new_board[i], slide_occur = slide(new_board[i])
        moved = moved or slide_occur
    if moved:
        add_new_tile(new_board)
    return new_board

def move_right(board):
    reversed_board = [row[::-1] for row in board]
    new_board = move_left(reversed_board)
    return [row[::-1] for row in new_board]

def move_up(board):
    transposed_board = [list(row) for row in zip(*board)]
    new_board = move_left(transposed_board)
    return [list(row) for row in zip(*new_board)]

def move_down(board):
    transposed_board = [list(row) for row in zip(*board)]
    new_board = move_right(transposed_board)
    return [list(row) for row in zip(*new_board)]

def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
    return True


def main():
    board = initialize_board()
    while True:
        print_board(board)
        if is_game_over(board):
            print("Game Over!")
            break
        direction = input("Enter direction (W/A/S/D): ").upper()
        if direction not in ['W', 'A', 'S', 'D']:
            print("Invalid direction! Use W/A/S/D.")
            continue
        if direction == 'W':
            board = move_up(board)
        elif direction == 'A':
            board = move_left(board)
        elif direction == 'S':
            board = move_down(board)
        elif direction == 'D':
            board = move_right(board)
        # add_new_tile(board)


if __name__ == "__main__":
    main()
