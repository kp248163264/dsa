# TODO: finish reading through this problem in Skiena, implement and test


def is_a_solution(a,k,input):
    return

def process_solution(a,k,input):
    return

def possible_values(x,y,board,possible):
    return

def next_square(x,y,board):
    return


def construct_candidates(a, k, board, c, ncandidates):
    DIMENSION = 9
    x = []
    y = []
    i = 0
    possible = [0] * (DIMENSION+1)
    board.move[k][x]
    board.move[k][y]
    ncandidates=0

    if x<0 and y<0: # no moves possible
        return

    possible_values(x,y,board, possible)
    for i in range(DIMENSION+1):


    next_square(x,y,board)
    board.move[k][x] = x
    board.move[k][y] = y

    ncandidates = 0


def backtrack(a,k,input):

    NMAX = 100
    c = [0] * NMAX
    ncandidates = [NMAX]
    finished = False

    if is_a_solution(a,k,input):
        process_solution(a,k,input)
    else:
        k+=1
        construct_candidates(a,k,input,c,ncandidates)
        for i in ncandidates[0]:
            a[k] = c[i]
            backtrack(a,k,input)
            if finished:
                return


def sudoku_solver(board):
    """Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    The '.' character indicates empty cells."""
    NMAX = 100
    a = [0] * NMAX
    backtrack(0,input)



if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]
   sudoku_solver(board)