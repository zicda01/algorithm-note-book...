import sys
sys.stdin = open("input.txt", "r")

N = int(input())

cnt = 1
num_sequence = 1
direction = 1

while N > num_sequence:
    cnt += 1
    num_sequence += cnt
    direction = direction * (-1)

if direction == -1:
    index = [cnt - (num_sequence - N), num_sequence - N + 1]
else:
    index = [num_sequence - N + 1, cnt - (num_sequence - N)]

x, y = index
print(f'{x}/{y}')