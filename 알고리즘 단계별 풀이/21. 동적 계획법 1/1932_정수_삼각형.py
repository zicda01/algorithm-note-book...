N = int(input())
triangle_matrix = [list(map(int, input().split())) for _ in range(N)]
result_matrix = [[0] * N for _ in range(N)]

result_matrix[0][0] = triangle_matrix[0][0]
for i in range(1, N):
    for j in range(0, i + 1):
        if j > 0 and j < i :
            result_matrix[i][j] = triangle_matrix[i][j] + max(result_matrix[i - 1][j - 1], result_matrix[i - 1][j])
        else:
            if j <= 0:
                result_matrix[i][j] = triangle_matrix[i][j] + result_matrix[i - 1][j]
            else:
                result_matrix[i][j] = triangle_matrix[i][j] + result_matrix[i - 1][j - 1]

print(max(result_matrix[N - 1]))