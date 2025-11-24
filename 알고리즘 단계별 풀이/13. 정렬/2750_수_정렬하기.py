# import sys
# input = sys.stdin.readline  # 이렇게 하면 input()처럼 사용 가능

import sys
sys.stdin = open("input.txt", "r")

# 삽입정렬 알고리즘을 사용한다.
N = int(input())
array = list()
for _ in range(N):
    array.append(int(input()))

for i in range(1, N):
    key = array[i]
    j = i - 1

    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key

for num in array:
    print(num)