import sys
sys.stdin = open("input.txt", "r")

word = input()
l = len(word)
set_result = set()
for i in range(l):
    for j in range(i + 1, l + 1):
        target_word = word[i:j]
        if target_word in set_result:
            continue
        set_result.add(target_word)

print(len(set_result))