import sys
sys.stdin = open("input.txt", "r")

# 원형큐를 popleft 와 append 를 이용해 흉내내기

from collections import deque
N = int(input())
array = list(map(int, input().split()))
baloons = deque()
for i in range(N):
    baloon_append_rule = (array[i], i + 1)
    baloons.append(baloon_append_rule)

top = 0
result = [0] * N
for i in range(N):
    if top > 0:
        for j in range(top - 1):
            temp = baloons.popleft()
            baloons.append(temp)


    elif top < 0:
        for j in range(abs(top)):
            temp = baloons.pop()
            baloons.appendleft(temp)

    else:
        pass

    target = baloons.popleft()
    result[i] = target[1]
    top = target[0]
print(*result)