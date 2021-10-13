def printSolution(board):
    for i in range(M):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
 
 
def countInColumns(board, ch, j):
    count = 0
    for i in range(M):
        if board[i][j] == ch:
            count = count + 1
    return count
 
 
def countInRow(board, ch, i):
    count = 0
    for j in range(N):
        if board[i][j] == ch:
            count = count + 1
    return count
 
 
def isSafe(board, row, col, ch, top, left, bottom, right):
 
    if ((row - 1 >= 0 and board[row - 1][col] == ch) or
            (col + 1 < N and board[row][col + 1] == ch) or
            (row + 1 < M and board[row + 1][col] == ch) or
            (col - 1 >= 0 and board[row][col - 1] == ch)):
        return False
 
    rowCount = countInRow(board, ch, row)
 
    colCount = countInColumns(board, ch, col)
 
    if ch == '+':
 
        if top[col] != -1 and colCount >= top[col]:
            return False
 
        if left[row] != -1 and rowCount >= left[row]:
            return False
 
    if ch == '-':
 
        if bottom[col] != -1 and colCount >= bottom[col]:
            return False
 
        if right[row] != -1 and rowCount >= right[row]:
            return False
 
    return True
 
 
def validateConfiguration(board, top, left, bottom, right):
 
    for i in range(N):
        if top[i] != -1 and countInColumns(board, '+', i) != top[i]:
            return False
 
    for j in range(M):
        if left[j] != -1 and countInRow(board, '+', j) != left[j]:
            return False
 
    for i in range(N):
        if bottom[i] != -1 and countInColumns(board, '-', i) != bottom[i]:
            return False
 
    for j in range(M):
        if right[j] != -1 and countInRow(board, '-', j) != right[j]:
            return False
 
    return True
 
 
def solveMagnetPuzzle(board, row, col, top, left, bottom, right, rules):
 
    if row >= M - 1 and col >= N - 1:
        return validateConfiguration(board, top, left, bottom, right)
 
    if col >= N:
        col = 0
        row = row + 1
 
    if rules[row][col] == 'R' or rules[row][col] == 'B':
 
        if solveMagnetPuzzle(board, row, col + 1, top, left, bottom, right, rules):
            return True
 
    if rules[row][col] == 'L' and rules[row][col + 1] == 'R':
 
        if (isSafe(board, row, col, '+', top, left, bottom, right) and
                isSafe(board, row, col + 1, '-', top, left, bottom, right)):
            board[row][col] = '+'
            board[row][col + 1] = '-'
 
            if solveMagnetPuzzle(board, row, col + 2, top, left, bottom, right, rules):
                return True
 
            board[row][col] = 'X'
            board[row][col + 1] = 'X'
 
        if (isSafe(board, row, col, '-', top, left, bottom, right) and
                isSafe(board, row, col + 1, '+', top, left, bottom, right)):
            board[row][col] = '-'
            board[row][col + 1] = '+'
 
            if solveMagnetPuzzle(board, row, col + 2, top, left, bottom, right, rules):
                return True
 
            board[row][col] = 'X'
            board[row][col + 1] = 'X'
 
    if rules[row][col] == 'T' and rules[row + 1][col] == 'B':
 
        if (isSafe(board, row, col, '+', top, left, bottom, right) and
                isSafe(board, row + 1, col, '-', top, left, bottom, right)):
            board[row][col] = '+'
            board[row + 1][col] = '-'
 
            if solveMagnetPuzzle(board, row, col + 1, top, left, bottom, right, rules):
                return True
 
            board[row][col] = 'X'
            board[row + 1][col] = 'X'
 
        if (isSafe(board, row, col, '-', top, left, bottom, right) and
                isSafe(board, row + 1, col, '+', top, left, bottom, right)):
            board[row][col] = '-'
            board[row + 1][col] = '+'
 
            if solveMagnetPuzzle(board, row, col + 1, top, left, bottom, right, rules):
                return True
 
            board[row][col] = 'X'
            board[row + 1][col] = 'X'
 
    if solveMagnetPuzzle(board, row, col + 1, top, left, bottom, right, rules):
        return True
 
    return False
 
 
def magnetPuzzle(top, left, bottom, right, rules):
 
    board = [['X' for x in range(N)] for y in range(M)]
 
    if not solveMagnetPuzzle(board, 0, 0, top, left, bottom, right, rules):
        print("Solution does not exist")
        return
 
    printSolution(board)
 
 
if __name__ == '__main__':
 
    top = [1, -1, -1, 2, 1, -1]
    bottom = [2, -1, -1, 2, -1, 3]
    left = [2, 3, -1, -1, -1]
    right = [-1, -1, -1, 1, -1]
 
    rules = [
        ['L', 'R', 'L', 'R', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B'],
        ['T', 'T', 'T', 'T', 'L', 'R'],
        ['B', 'B', 'B', 'B', 'T', 'T'],
        ['L', 'R', 'L', 'R', 'B', 'B']
    ]
 
    (M, N) = (len(rules), len(rules[0]))
 
    magnetPuzzle(top, left, bottom, right, rules)
