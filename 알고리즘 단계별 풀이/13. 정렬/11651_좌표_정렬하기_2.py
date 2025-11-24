import sys
sys.stdin = open("input.txt", "r")

# 병합정렬을 이용해 풀이하는 것이 알고리즘 관점의 풀이이다.
# y 좌표를 기준으로 병합정렬의 merge를 수행하고, y 좌표가 같은 경우 x 좌표를 비교하는 조건을 추가해서, 의도한 정렬을 수행할 수 있다.

N = int(input())
address_array = list()
for i in range(N):
    x, y = map(int, input().split())
    address_array.append([x, y])
address_array.sort(key=lambda address:(address[1], address[0]))

for address in address_array:
    print(*address)