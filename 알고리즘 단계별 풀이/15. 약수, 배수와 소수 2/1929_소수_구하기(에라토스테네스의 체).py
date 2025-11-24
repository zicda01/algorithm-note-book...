import sys
sys.stdin = open("input.txt", "r")

# 소수의 배열을 반환하는 가장 빠른 알고리즘은 '에라토스테네스의 체'이다.

N, M = map(int, input().split())
prime_list = [True] * (M + 1)
prime_list[0] = prime_list[1] = False
for i in range(2, int(M ** 0.5) + 1):
    if prime_list[i] == True:
        for j in range(i * i, M + 1, i):
            prime_list[j] = False
for num in range(N, M + 1):
    if prime_list[num]:
        print(num)