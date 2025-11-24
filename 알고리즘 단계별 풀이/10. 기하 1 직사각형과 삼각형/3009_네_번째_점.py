# import sys
# input = sys.stdin.readline  # 이렇게 하면 input()처럼 사용 가능

import sys
sys.stdin = open("input.txt", "r")

# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

w_array = list()
h_array = list()
for _ in range(3):
    temp_array = list(map(int, input().split()))
    w_array.append(temp_array[0])
    h_array.append(temp_array[1])

w = h = 0
for i in range(3):
    if w_array.count(w_array[i]) == 1:
        w = w_array[i]
    if h_array.count(h_array[i]) == 1:
        h = h_array[i]
print(w, h)