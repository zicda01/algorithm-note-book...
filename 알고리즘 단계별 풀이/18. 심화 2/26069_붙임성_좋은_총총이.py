import sys
sys.stdin = open("input.txt", "r")

N = int(input())
dance_people = set()
dance_people.add("ChongChong")
for _ in range(N):
    A, B = input().split()
    if A in dance_people:
        dance_people.add(B)
    elif B in dance_people:
        dance_people.add(A)
    else:
        continue
print(len(dance_people))