import random

#generates a random board with the given dimensions.
def random_board(length, width):
    possible_tiles = ['-', '-', '-', '$']
    return [[possible_tiles[random.randint(0,3)] for i in range(length)] for j in range(width)]

#returns the number of uncleared tiles in the board
def money_left(board):
    return sum([len([val for val in row if val == '$']) for row in board])

#moves karel using the given move function
def move_karel(karel, length, width, move_function):
    change = move_function(karel[0], karel[1], length, width)
    if change == "UP":
        karel[1] -= 1
    if change == "DOWN":
        karel[1] += 1
    if change == "LEFT":
        karel[0] -= 1
    if change == "RIGHT":
        karel[0] += 1

#a very basic moving algorithm: can you do better?
def dumb_move(cur_x, cur_y, board_length, board_width):
    if cur_x == 0 and cur_y % 2 == 1:
        return "DOWN"
    elif cur_x == board_length - 1 and cur_y % 2 == 0:
        return "DOWN"
    elif cur_y % 2 is 0:
        return "RIGHT"
    else:
        return "LEFT"

#nicely prints board!
def print_board(board):
    for row in board:
        print("".join(row))

#runs the karel program
if __name__ == "__main__":
    #initialize board and karel position
    length, width = 5,5
    board = random_board(length, width)
    karel = [0,0]
    print_board(board)
    #note that you shouldn't take more than 25 moves, the dumb solution
    for i in range(2 * length * width):
        print(karel)
        if board[karel[0]][karel[1]] == '$':
            board[karel[0]][karel[1]] = '-'
        if money_left(board) == 0:
            print("%d moves total" % i)
            break
        move_karel(karel, length, width, dumb_move)
    if money_left(board) > 0:
        print("Uh oh! Your karel didn't pick up all the money!")
        
