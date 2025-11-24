# ord('A') → 65

import sys
sys.stdin = open("input.txt", "r")

N, B = input().split()

radix = int(B)
num_fliter = '0123456789'
num_box = list()
for num in N:
    if num in num_fliter:
        num_box.append(int(num))
    else:
        num_box.append(ord(num) - 55)

num_box.reverse()
digits = len(num_box)

result = 0
for i in range(digits):
   result += num_box[i] * (radix ** i)

print(result)