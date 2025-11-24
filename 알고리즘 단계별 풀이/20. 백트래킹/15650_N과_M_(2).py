import sys
sys.stdin = open("input.txt", "r")

# 중복이 허용되지 않은 조합(Combination)

def combination(index, limit, depth):

    global result

    if depth == M:
        print(*result)
        return

    if index == limit:
        return

    for i in range(index + 1, limit + 1):
        result.append(i)
        combination(i, limit, depth + 1)
        result.pop()

    return

N, M = list(map(int, input().split()))

result = list()

combination(0, N, 0)