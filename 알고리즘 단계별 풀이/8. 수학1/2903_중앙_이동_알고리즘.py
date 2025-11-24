import sys
sys.stdin = open("input.txt", "r")

N = int(input())    # N번 거친 후 점의 수를 출력

# 초기 상태, 한 변에 점이 두 개 있다. ... = n0
# N = 1 의 상태, 한 변에 점이 세 개 있다. (2 + 1) ... = n1 = n0 + n0 - 1
# N = 2 의 상태, 한 변에 점이 다섯 개 있다. (3 + 2) ... -> 5 = n1 + n1 - 1
# N = 3 의 상태, 한 변에 점이 아홉 개 있다. (5 + 4) ... -> 9 = n2 + n2 - 1
# ...
# N = n 의 상태, 한 변에 점이
initial_num = 2
num = initial_num
temp = 0

for _ in range(N):
    temp = num*2 - 1
    num = temp

print(num**2)