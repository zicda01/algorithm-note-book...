import sys
sys.stdin = open("input.txt", "r")

N = int(input())
check_list = set()
cnt = 0
for _ in range(N):
    input_chat = input()
    if input_chat == "ENTER":
        check_list = set()
        continue

    if input_chat in check_list:
        continue

    check_list.add(input_chat)
    cnt += 1
print(cnt)