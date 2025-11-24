N = int(input())

cnt = 0
visited_column = [0] * N
visited_diagonal_1 = [0] * (N * 2 - 1)
visited_diagonal_2 = [0] * (N * 2 - 1)

def nQueen(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for i in range(N):
        if visited_column[i] or visited_diagonal_1[i + row] or visited_diagonal_2[i - row + N - 1]:
            continue
        visited_column[i] = 1
        visited_diagonal_1[i + row] = 1
        visited_diagonal_2[i - row + N - 1] = 1
        nQueen(row + 1)
        visited_column[i] = 0
        visited_diagonal_1[i + row] = 0
        visited_diagonal_2[i - row + N - 1] = 0

    return

nQueen(0)

print(cnt)