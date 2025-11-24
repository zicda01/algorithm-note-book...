import sys
sys.stdin = open("input.txt","r")

N, M = map(int, input().split())
hard_to_listen = set()
hard_to_hear = set()
for _ in range(N):
    hard_to_listen.add(input())
for _ in range(M):
    hard_to_hear.add(input())
hard_to_listen_and_hear = hard_to_listen & hard_to_hear
hard_to_listen_and_hear = sorted(list(hard_to_listen_and_hear))

print(len(hard_to_listen_and_hear))
for data in hard_to_listen_and_hear:
    print(data)