import sys
sys.stdin = open("input.txt", "r")

from collections import deque

N = int(sys.stdin.readline())
deck = deque()
for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    case = command[0]
    if case == 1:
        deck.appendleft(command[1])
    elif case == 2:
        deck.append(command[1])
    elif case == 3:
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif case == 4:
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif case == 5:
        print(len(deck))
    elif case == 6:
        if deck:
            print(0)
        else:
            print(1)
    elif case == 7:
        if deck:
            print(deck[0])
        else:
            print(-1)
    else:
        if deck:
            print(deck[len(deck) - 1])
        else:
            print(-1)