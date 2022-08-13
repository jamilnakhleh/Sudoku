board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ",end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ",end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
    return None


def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #Check boardx
    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3

    for i in range(boardx_y * 3, boardx_y * 3 + 3):
        for j in range(boardx_x * 3, boardx_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True # we found the soluion
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):# check if by adding those into the boardard it would be valid solution
            board[row][col] = i # full the boardard
            if solve(board): # call the function with new value-added and keep trying until we find a solution
                return True
            board[row][col] = 0 # We are backtrack - last element  we added cant be correct.
    return False


print("Sudoku board before running the solution :")
print_board(board)
solve(board)
print("____________________________________________________________________________________")
print("Sudoku board after running the solution :")
print_board(board)
