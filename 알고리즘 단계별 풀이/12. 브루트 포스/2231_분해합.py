# import sys
# input = sys.stdin.readline  # 이렇게 하면 input()처럼 사용 가능

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
digit_calculation = N
digit_cnt = 0
is_generated = False
while digit_calculation > 0:
    digit_calculation = digit_calculation // 10
    digit_cnt += 1
target_num = N
min_target = float('inf')
minus_cnt = 0
while target_num > 0:
    minus_cnt += 1
    target_num = N - minus_cnt
    remainder = 0
    temp_target = target_num
    remainder_sum = 0
    while True:
        remainder = temp_target % 10
        temp_target = temp_target // 10
        remainder_sum += remainder
        if temp_target == 0:
            break

    if target_num + remainder_sum == N and min_target > target_num:
        min_target = target_num
        is_generated = True
    if minus_cnt > digit_cnt * 9:
        break
if is_generated:
    print(min_target)
else:
    print(0)