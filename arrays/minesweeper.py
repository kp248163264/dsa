
numbers = {"1", "2", "3", "4", "5", "6", "7", "8"}

def count_surrounding_mines_and_get_neighbors(board, row, col):
    ROWMIN = row-1
    ROWMAX=row+1
    if ROWMIN < 0:
        ROWMIN = row
    if ROWMAX >= len(board):
        ROWMAX = row

    COLMIN = col - 1
    COLMAX = col + 1
    if COLMIN < 0:
        COLMIN = col
    if COLMAX >= len(board[0]):
        COLMAX = col

    neighbors = []
    minecount = 0
    for r in range(ROWMIN, ROWMAX+1):
        for c in range(COLMIN, COLMAX+1):
            if not (r == row and c == col):
                neighbors.append((r, c))
                if board[r][c] == 'M':
                    minecount += 1
    return neighbors, minecount

def updateBoardHelper(board, row, col):
    neighbors, surrounding_mine_count = count_surrounding_mines_and_get_neighbors(board,row,col)
    surrounding_mine_count = sum([board[x][y] == "M" for x, y in neighbors])
    if surrounding_mine_count!=0:
        board[row][col] = surrounding_mine_count
        return
    elif board[row][col] == "E":
        board[row][col] = "B"
        for r, c in neighbors:
            if board[r][c] == 'E':
                updateBoardHelper(board, r, c)
    return board

def updateBoard(board, click):
    row, col = click[0], click[1]
    if board[row][col] == "M":
        board[row][col] = "X"
        print(board)
        return board
    res = updateBoardHelper(board, row, col)
    print(res)
    return res


if __name__ == '__main__':
    board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
    click = [1,2]
    updateBoard(board, click)
