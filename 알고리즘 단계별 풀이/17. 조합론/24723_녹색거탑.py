import sys
sys.stdin = open("input.txt", "r")

# 단순히 print(2 ** N) 으로 풀 수도 있지만...

N = int(input())
def dfs(n, level):
    global cnt
    if n == level:
        cnt += 1
        return
    dfs(n + 1, level)
    dfs(n + 1, level)
    return

cnt = 0

dfs(0, N)
print(cnt)