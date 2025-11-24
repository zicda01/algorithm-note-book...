import sys
sys.stdin = open("input.txt", "r")

# 중복이 허용된 순열(Permutation)

def combination(limit, depth):

    global result

    if depth == M:
        print(*result)
        return

    for i in range(1, limit + 1):
        result.append(i)
        combination(limit, depth + 1)
        result.pop()

    return

N, M = list(map(int, input().split()))

result = list()

combination(N, 0)