import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    factorial_n = 1
    factorial_m = 1
    for i in range(1, N + 1):
        factorial_n = factorial_n * i
        factorial_m = factorial_m * M
        M -= 1
    print(factorial_m // factorial_n)