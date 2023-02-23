

# def getAdjacent(board, row, col):
#     ROWMIN = row-1
#     ROWMAX = row+1
#     if ROWMIN < 0:
#         ROWMIN = row
#     if ROWMAX >= len(board):
#         ROWMAX = row
#
#     COLMIN = col-1
#     COLMAX = col+1
#     if COLMIN < 0:
#         COLMIN = col
#     if COLMAX >= len(board[0]):
#         COLMAX = col
#
#     adj = []
#     for r in range(ROWMIN, ROWMAX+1):
#         for c in range(COLMIN, COLMAX+1):
#             if not (r==row and c==col):
#                 adj.append((r, c))
#     return adj
#
#
#
# def updateBoardHelper(board, row, col):
#
#     queue = [(row, col)]
#     while queue:
#         r, c = queue.pop(0)
#         adj = getAdjacent(board, r, c)
#         countAdjMines = sum([1 if board[i][j] == "M" else 0 for (i, j) in adj])
#         if countAdjMines:
#             board[r][c] = countAdjMines
#         else:
#             board[r][c] = "B"
#             for ro, co in adj:
#                 if board[ro][co] == "E":
#                     queue.append((ro, co))
#     return board
#
#
# def updateBoard(board, click):
#     row = click[0]
#     col = click[1]
#     if board[row][col] == "M":
#         board[row][col] = "X"
#         return board
#     return updateBoardHelper(board, row, col)
#
#

#
#
# def getAdjacent(board, row, col):
#     ROWMAX = row+1
#     ROWMIN = row-1
#     if ROWMAX >= len(board):
#         ROWMAX = row
#     if ROWMIN < 0:
#         ROWMIN = row
#
#     COLMAX = col + 1
#     COLMIN = col - 1
#     if COLMAX >= len(board[0]):
#         COLMAX = col
#     if COLMIN < 0:
#         COLMIN = col
#
#     adj = []
#     for r in range(ROWMIN, ROWMAX+1):
#         for c in range(COLMIN,COLMAX+1):
#             if not (r == row and c == col):
#                 adj.append((r, c))
#     return adj
#
#
#
#
# def updateBoardHelper(board, row, col):
#     # Run-time of BFS: O(V+E), where V is number of vertices, E is number of edges
#     queue = [(row,col)]
#     while queue:
#         ro,co = queue.pop(0)
#         adj = getAdjacent(board,ro,co)
#         countAdjMines = sum([1 if board[i][j] == "M" else 0 for (i,j) in adj])
#         if countAdjMines:
#             board[ro][co] = countAdjMines
#         else:
#             board[ro][co] = "B"
#             for (r,c) in adj:
#                 if board[r][c] == "E":
#                     queue.append((r,c))
#     return board
#
#
#
#
#
#
#
# def updateBoard(board, click):
#     row = click[0]
#     col = click[1]
#     if board[row][col] == "M":
#         board[row][col] = "X"
#         return board
#     return updateBoardHelper(board, row, col)
#
#
#
#


def getAdjacent(board, row, col):
    ROWMAX = row + 1
    ROWMIN = row - 1
    if ROWMAX >= len(board):
        ROWMAX = row
    if ROWMIN < 0:
        ROWMIN = row

    COLMAX = col + 1
    COLMIN = col - 1
    if COLMAX >= len(board[0]):
        COLMAX = col
    if COLMIN < 0:
        COLMIN = col

    adj = []
    for r in range(ROWMIN, ROWMAX + 1):
        for c in range(COLMIN, COLMAX + 1):
            if not (r == row and c == col):
                adj.append((r,c))
    return adj



def updateBoardHelper(board, row, col):
    queue = [(row,col)]

    while queue:
        row,col = queue.pop(0)
        adj = getAdjacent(board, row, col)
        mine_count = sum([1 if board[r][c] == "M" else 0 for r,c in adj])
        if mine_count:
            board[row][col] = mine_count
        else:
            board[row][col] = "B"
            for (r,c) in adj:
                if board[r][c] == "E":
                    queue.append((r,c))
    return board



def updateBoard(board, click):
    row = click[0]
    col = click[1]
    b = updateBoardHelper(board, row, col)
    return b





if __name__ == "__main__":
    board = ["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]
    click = [3,0]
    b = updateBoard(board, click)
    print(b)