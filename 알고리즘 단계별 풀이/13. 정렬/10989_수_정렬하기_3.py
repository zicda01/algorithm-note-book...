import sys

# 인덱스 카운팅 배열을 이용한다.

MAX_NUM = 10001
counts = [0] * MAX_NUM

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(MAX_NUM):
    for _ in range(counts[i]):
        sys.stdout.write(str(i) + '\n')