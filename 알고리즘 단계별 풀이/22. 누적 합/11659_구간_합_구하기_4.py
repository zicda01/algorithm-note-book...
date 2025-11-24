import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

prefix_sums = [0] * N
prefix_sum = 0
for i in range(N):
    prefix_sum = prefix_sum + numbers[i]
    prefix_sums[i] = prefix_sum

prefix_sums = [0] + prefix_sums

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    result = prefix_sums[end] - prefix_sums[start - 1]
    print(result)