import sys
sys.stdin = open("input.txt", "r")

# 정수 범위가 계산가능한 수준으로 점해져있으므로,
# 미리 모든 케이스를 포함한 소수 배열을 만들어두고,
# 범위에 대해 계산하는 방식으로 풀이하는 게 효율적.

l = 246912
prime_list = [True] * (l + 1)
prime_list[0] = prime_list[1] = False
for i in range(2, int(l ** 0.5) + 1):
    if prime_list[i]:
        for j in range(i * i, l + 1, i):
            prime_list[j] = False

while True:
    n = int(input())
    if not n:
        break
    m = n * 2
    prime_cnt = 0
    for k in range(n + 1, m + 1):
        if prime_list[k]:
            prime_cnt += 1
    print(prime_cnt)