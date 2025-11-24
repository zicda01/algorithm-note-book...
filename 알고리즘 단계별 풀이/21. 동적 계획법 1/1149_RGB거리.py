import sys
sys.stdin = open("input.txt", "r")

N = int(input())

rgb_matrix = list()
for i in range(N):
    rgb_matrix.append(list(map(int, input().split())))

result_matrix = [[0] * 3 for _ in range(N)]

for i in range(3):
    result_matrix[0][i] = rgb_matrix[0][i]

def find_min(array, index):
    min_value = 1000 * 1000
    for i in range(3):
        if i != index and array[i] < min_value:
            min_value = array[i]
    return min_value

for i in range(1, N):
    for j in range(3):
        # i 는 level, j 는 r, g, b
        result_matrix[i][j] = rgb_matrix[i][j] + find_min(result_matrix[i - 1], j)

print(min(result_matrix[N - 1]))