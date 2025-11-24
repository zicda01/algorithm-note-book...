import sys
sys.stdin = open("input.txt", "r")

N = int(input())
cnt = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        cnt += 1

print(cnt)