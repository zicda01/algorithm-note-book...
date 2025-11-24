# import sys
# input = sys.stdin.readline  # 이렇게 하면 input()처럼 사용 가능

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
array = list(map(int, input().split()))

cnt = 0

for i in range(N):
    is_prime = True
    num = array[i]
    for j in range(2, num//2 + 1):
        if num % j == 0:
            is_prime = False
            break

    if num != 1 and is_prime:
        cnt += 1
print(cnt)