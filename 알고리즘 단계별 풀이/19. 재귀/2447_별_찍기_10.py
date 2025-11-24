import sys
sys.stdin = open("input.txt", "r")

def cantor_sqaure(x, y, size, matrix):

    if size == 1:
        return

    size = size // 3

    for i in range(x + size, x + 2 * size):
        for j in range(y + size, y + 2 * size):
            matrix[i][j] = " "

    for i in range(3):
        for j in range(3):
            if size == 1:
                continue
            if i == 1 and j == 1:
                continue
            cantor_sqaure(x + i * size, y + j * size, size, matrix)

    return

N = int(input())
cantor_matrix = [["*"] * N for _ in range(N)]

cantor_sqaure(0, 0, N, cantor_matrix)

for row in cantor_matrix:
    print(*row, sep='')