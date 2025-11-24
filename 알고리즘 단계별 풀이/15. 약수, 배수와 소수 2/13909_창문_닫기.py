import sys
sys.stdin = open("input.txt", "r")

# 모든 창문은 닫혀 있는 상태로 시작.
# N 번째 창문에 대해서, N의 약수가 짝수 개라면 창문이 닫혀 있을 것이고,
# N의 약수가 홀수 개라면, 창문이 열려 있게 된다.
# 약수는 (x, y) 형태로 한 쌍으로 존재한다고 볼 수 있고,
# 약수가 홀수 개가 되려면, N은 (x, x) 형태의 제곱수여야 한다.


N = int(input())
open_windows = int(N ** 0.5)
print(open_windows)
