import sys
sys.stdin = open("input.txt", "r" )

# 통분 이후에 최대공약수를 구해서, 분자와 분모를 각각 나눠준다.

numerator_a, denominator_a = map(int, input().split())
numerator_b, denominator_b = map(int, input().split())
denominator_ab = denominator_a * denominator_b
numerator_ab = (numerator_a * denominator_b) + (numerator_b * denominator_a)

target_num = denominator_ab
divisor = numerator_ab
while target_num % divisor:
    temp = divisor
    divisor = target_num % divisor
    target_num = temp
gcd = divisor

new_numerator = numerator_ab // gcd
new_denominator = denominator_ab // gcd
reduced_fraction = [new_numerator, new_denominator]
print(*reduced_fraction)