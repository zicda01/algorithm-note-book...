import sys
sys.stdin = open("input.txt", "r")

N = int(input())

factors = list(map(int, input().split()))
factors.sort()

if N == 1:
    print(factors[0] ** 2)
else:
    print(factors[0] * factors[N - 1])
