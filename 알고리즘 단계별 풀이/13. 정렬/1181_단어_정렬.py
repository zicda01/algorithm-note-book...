import sys
sys.stdin = open("input.txt", "r")

N = int(input())
words_array = list()
for _ in range(N):
    word = input()
    if word in words_array:
        continue
    words_array.append(word)

words_array.sort(key=lambda x:(len(x), x))
for word in words_array:
    print(word)