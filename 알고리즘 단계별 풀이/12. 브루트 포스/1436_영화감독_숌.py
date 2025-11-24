# import sys
# input = sys.stdin.readline  # 이렇게 하면 input()처럼 사용 가능

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num = 0
cnt = 0
while True:
    num += 1
    if '666' in str(num):
        cnt += 1
    if cnt == N:
        break
print(num)