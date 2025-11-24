def sudoku(depth):
    if depth == limit_depth:
        return True

    r, c = zero_list[depth]
    for n in range(1, 10):
        if not row_check(n, r, c) or not column_check(n, r, c) or not square_check(n, r, c):
            continue
        matrix[r][c] = n
        if sudoku(depth + 1):
            return True
        matrix[r][c] = 0
    return False

def row_check(N, R, C):
    for i in range(9):
        if N == matrix[R][i]:
            return False
    return True

def column_check(N, R, C):
    for i in range(9):
        if N == matrix[i][C]:
            return False
    return True

def square_check(N, R, C):
    r_square = (R // 3) * 3
    c_square = (C // 3) * 3
    for r in range(r_square, r_square + 3):
        for c in range(c_square, c_square + 3):
            if N == matrix[r][c]:
                return False
    return True

matrix = [list(map(int, input().split())) for _ in range(9)]

zero_list = list()
limit_depth = 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            zero_list.append((i, j))
            limit_depth += 1

sudoku(0)

for array in matrix:
    print(*array)