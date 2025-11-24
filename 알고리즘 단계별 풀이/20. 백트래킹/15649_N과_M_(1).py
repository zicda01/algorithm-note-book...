# 중복이 허용되지 않는 순열(Permutation)

def recurssion_combination(Array, Depth, Result, Visited):
    if Depth == M:
        print(*Result)
        return
    for i in range(N):
        if Visited[i]:
            continue
        Visited[i] = 1
        Result[Depth] = Array[i]
        recurssion_combination(Array, Depth + 1, Result, Visited)
        Visited[i] = 0

    return

N, M = map(int, input().split())
numbers = list(range(1, N + 1))

depth = 0
result = [0] * M
visited = [0] * N
recurssion_combination(numbers, depth, result, visited)
