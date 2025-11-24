import sys
sys.stdin = open("input.txt", "r")

n, k = list(map(int, input().split()))

factorial_k = 1
factorial_n = 1
for i in range(1, k + 1):
    factorial_k = factorial_k * i
    factorial_n = factorial_n * n
    n -= 1

print(factorial_n // factorial_k)