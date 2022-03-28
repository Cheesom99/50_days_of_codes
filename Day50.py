board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):  # a fxn for solving
    find = find_empty(bo)  # set another fxn equals to find
    if not find:  # if no empty cell, return true
        return True
    else:  # if there is empty cell
        row, col = find
    for i in range(1, 10):
        if valid_board(board, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False


def valid_board(bo, num, pos):  # Checking if the given board is valid
    # check row (loop through every col in the given row)
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:  # check row and if it's pos we just inserted, we ignore that position
            return False
    # check col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:  # if it's pos we just inserted, we ignore that position
            return False
    # check box
    box_x = pos[1] // 3  # col / 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != i:
                return False

    return True


def print_board(bo):  # fxn to display board
    for i in range(len(bo)):  # for the range of the rows
        if i % 3 == 0 and i != 0:  # to make the row lines to be in threes
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):  # for the range of the 1st row
            if j % 3 == 0 and j != 0:  # to make the column line to be in threes
                print(" | ", end="")  # print '|'... the 'end' is to arrange it in threes
            if j == 8:  # at the column 8, print corresponding number
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ", end="")  # at other cols, print number, including a space


print_board(board)


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None


# print_board(board)
solve(board)
print(".....................................")
print_board(board)
