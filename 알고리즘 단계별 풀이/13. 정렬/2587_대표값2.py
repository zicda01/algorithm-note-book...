# import sys
# input = sys.stdin.readline  # 이렇게 하면 input()처럼 사용 가능

import sys
sys.stdin = open("input.txt", "r")

# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

# 삽입정렬 알고리즘을 사용한다.
N = 5
array = [0] * N
for i in range(N):
    array[i] = int(input())

for j in range(1, N):
    key = array[j]
    k = j - 1
    while k >= 0 and key < array[k]:
        array[k + 1] = array[k]
        k -= 1
    array[k + 1] = key

array_sum = 0
for num in array:
    array_sum += num

array_mean = int(array_sum / N)
array_median = array[int((N - 1) / 2)]

print(array_mean)
print(array_median)