import sys
sys.stdin = open("input.txt", "r")

from collections import deque

N = int(input())
queue = deque(range(1, N + 1))
switch = 1
while True:
    if len(queue) == 1:
        break
    if switch:
        queue.popleft()
        switch = 1 - switch
    else:
        card_going_top = queue.popleft()
        queue.append(card_going_top)
        switch = 1 - switch
print(queue[0])