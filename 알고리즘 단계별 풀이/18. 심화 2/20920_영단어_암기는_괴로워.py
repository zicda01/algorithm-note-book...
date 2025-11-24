import sys
sys.stdin = open("input.txt", "r")

N, M = list(map(int, sys.stdin.readline().strip().split()))

word_list = list()
word_count = dict()
for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) < M:
        continue
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 0
        word_list.append(word)

word_list.sort(key=lambda x:(-word_count[x], -len(x), x))

for word in word_list:
    sys.stdout.write(word + '\n')