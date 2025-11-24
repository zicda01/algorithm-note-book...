import sys
sys.stdin = open("input.txt", "r")

# 중복이 허용된 조합(Combination)

def func_backtrack(start, limit, depth):
    global result

    if depth == M:
        print(*result)
        return

    for idx in range(start, limit + 1):
        result.append(idx)
        func_backtrack(idx, limit, depth + 1)
        result.pop()

    return

N, M = list(map(int, input().split()))

# 1부터 N까지 정수에 대해, M개의 수를 뽑아 중복이 허용되는 조합을 만든다.

result = list()

func_backtrack(1, N, 0)