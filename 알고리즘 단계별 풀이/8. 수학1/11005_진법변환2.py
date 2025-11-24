# ord('A') → 65
# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.

import sys
sys.stdin = open("input.txt", "r")

N, B = input().split()

target_num = int(N)
radix = int(B)
cnt = 0

array = list()
while True:
    # quotient
    # remainder
    quotient = target_num // radix
    remainder = target_num % radix
    if remainder > 9:
        remainder = chr(remainder + 55)
    else:
        remainder = str(remainder)

    if target_num > 0:
        target_num = quotient
        array.append([cnt, remainder])
        cnt += 1
    else:
        break

# print(array)

result = str()
for data in array:
    result = data[1] + result

print(result)