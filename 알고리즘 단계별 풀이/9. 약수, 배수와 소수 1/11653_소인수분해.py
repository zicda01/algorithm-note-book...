import sys
sys.stdin = open("input.txt", "r")

# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

N = int(input())
target_num = N
factor_box = list()

divisor = 2

while divisor < N + 1:
    if target_num % divisor == 0:
        factor_box.append(divisor)
        print(divisor)
        target_num = target_num // divisor
    else:
        divisor += 1
