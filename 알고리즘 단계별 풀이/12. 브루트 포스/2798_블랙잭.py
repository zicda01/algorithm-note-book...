# import sys
# input = sys.stdin.readline  # 이렇게 하면 input()처럼 사용 가능

import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
cards = list(map(int, input().split()))
max_combination = 0
temp_sum = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            temp_sum = cards[i] + cards[j] + cards[k]
            if temp_sum > M:
                continue
            if max_combination < temp_sum:
                max_combination = temp_sum
print(max_combination)