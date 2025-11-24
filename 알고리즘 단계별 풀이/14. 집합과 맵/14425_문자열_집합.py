import sys
sys.stdin = open("input.txt", "r")

# set, in 을 활용하여 포함관계를 검사한다.

N, M = map(int, input().split())
words_set = set()
cnt = 0
for _ in range(N):
    words_set.add(input())
for _ in range(M):
    target_word = input()
    if target_word in words_set:
        cnt += 1

print(cnt)