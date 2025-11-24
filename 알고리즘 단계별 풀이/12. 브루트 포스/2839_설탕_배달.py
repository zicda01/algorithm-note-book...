# import sys
# input = sys.stdin.readline  # 이렇게 하면 input()처럼 사용 가능

import sys
sys.stdin = open("input.txt", "r")

N = int(input())

min_cnt = 5000
for x in range((N // 5) + 1):
    for y in range((N // 3) + 1):
        if (5 * x) + (3 * y) == N:
            temp_cnt = x + y
            if min_cnt > temp_cnt:
                min_cnt = temp_cnt
if min_cnt != 5000:
    print(min_cnt)
else:
    print(-1)