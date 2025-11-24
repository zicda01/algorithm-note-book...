import sys
sys.stdin = open("input.txt", "r")

def hanoi_tower(start, help, goal, n, path):

    if n == 1:
        ring = start[1].pop()
        path.append((start[0], goal[0]))
        goal[1].append(ring)
        return

    hanoi_tower(start, goal, help, n - 1, path)
    hanoi_tower(start, help, goal, 1, path)
    hanoi_tower(help, start, goal, n - 1, path)

    return

N = int(input())

tower_1 = [1, list(range(N, 0, -1))]
tower_2 = [2, list()]
tower_3 = [3, list()]
cnt = 0
path = list()

hanoi_tower(tower_1, tower_2, tower_3, N, path)
print(len(path))
for record in path:
    print(*record)