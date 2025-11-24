import sys
sys.stdin = open("input.txt", "r")

# N의 약수 중에서, K번째로 작은 수를 출력한다.
# 존재하지 않는 경우 0을 출력한다.
N, K = map(int, input().split())

sequence_count = 0
for i in range(1, N + 1):
    if not(N % i):
        sequence_count += 1

    if sequence_count == K:
        print(i)
        break

if sequence_count < K:
    print(0)