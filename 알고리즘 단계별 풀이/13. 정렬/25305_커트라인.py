import sys
sys.stdin = open("input.txt", "r")

N, k = map(int, input().split())
scores = list(map(int, input().split()))

# 삽입정렬을 이용해 내림차순 정렬을 구현한다.

for i in range(1, N):
    key = scores[i]
    j = i - 1
    while j >= 0 and key > scores[j]:
        scores[j + 1] = scores[j]
        j -= 1
    scores[j + 1] = key

print(scores[k - 1])