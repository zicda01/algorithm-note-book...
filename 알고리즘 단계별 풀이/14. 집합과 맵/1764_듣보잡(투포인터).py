import sys
sys.stdin = open("input.txt","r")

# 투포인터 알고리즘을 이용한다면?

N, M = map(int, input().split())
hard_to_listen = [""] * N
hard_to_hear = [""] * M
for n in range(N):
    hard_to_listen[n] = input()
for m in range(M):
    hard_to_hear[m] = input()

hard_to_listen.sort()
hard_to_hear.sort()
p1 = p2 = 0
hard_to_listen_and_hear = list()
while p1 < N and p2 < M:
    man_h2l = hard_to_listen[p1]
    man_h2h = hard_to_hear[p2]
    if man_h2l == man_h2h:
        hard_to_listen_and_hear.append(man_h2l)
        p1 += 1
        p2 += 1
    elif man_h2l < man_h2h:
        p1 += 1
    else: # man_h2l > man_h2h:
        p2 += 1

print(len(hard_to_listen_and_hear))
for man in hard_to_listen_and_hear:
    print(man)