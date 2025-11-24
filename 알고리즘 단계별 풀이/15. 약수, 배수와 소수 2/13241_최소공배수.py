import sys
sys.stdin = open("input.txt", "r")

# 유클리드 호제법을 이용해서 최대공약수, 최소공배수를 계산한다.

A, B = map(int,input().split())

divisor = A
target_num = B
while target_num % divisor:
    temp = target_num
    target_num = divisor
    divisor = temp % divisor
greatest_common_divisor = divisor
least_common_multiple = (A * B) // greatest_common_divisor
print(least_common_multiple)