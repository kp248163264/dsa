
def get_adjacent(board,row,col):
    #adj = lambda x,y : [(x+dx, y+dy) for dx in range(-1,2) for dy in range(-1,2) if (dx!=0 or dy!=0) and 0<=x+dx<len(board) and 0<=y+dy<len(board[0])]
    adj = lambda x, y: [(x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2)
                          if (dx or dy) and 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0])]


    # adj = lambda x,y: [(y+dy,x+dx) for dy in range(-1,2) for dx in range(-1,2) if not(dx==0 or dy==0)
    #                    and 0<=x+dx<len(board[0]) and 0 <= y+dy <len(board)]

    res = adj(row,col)
    print(res)
    return adj(row,col)

def get_adjacent_non_list_comp(board,row,col):
    ROWMIN = row-1
    ROWMAX = row+1
    COLMIN = col-1
    COLMAX = col+1
    if ROWMIN<0:
        ROWMIN = row
    if ROWMAX >= len(board):
        ROWMAX = row
    if COLMIN<0:
        COLMIN = col
    if COLMAX >= len(board[0]):
        COLMAX = col
    adj = 0
    for r in range(ROWMIN, ROWMAX + 1):
        for c in range(COLMIN, COLMAX+1):
            if not (r==row and c==col):
                adj.append(board[r][c])
    return adj

def minesweep(board, row, col):
    adj = get_adjacent(board,row,col)
    mine_count_adj = sum([1 if board[y][x] == "M" else 0 for (y,x) in adj])
    if mine_count_adj:
        board[row][col] = str(mine_count_adj)
        return
    else:
        board[row][col] = "B"
        for y,x in adj:
            if board[y][x] == "E":
                minesweep(board, y, x)
        return

def minesweeper(board, click):
    row = click[0]
    col = click[1]
    if board[row][col] == "M":
        board[row][col] = 'X'
        return board
    minesweep(board,row,col)

if __name__ == '__main__':
    board = ["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]
    click = [3,0]
    minesweeper(board,click)
    print(board)