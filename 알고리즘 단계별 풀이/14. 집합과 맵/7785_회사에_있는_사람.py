import sys
sys.stdin = open("input.txt", "r")

N = int(input())
people_stayed = list()
people_dict = dict()
idx = 0
for _ in range(N):
    person, action = input().split()
    if action == "enter":
        people_stayed.append(person)
        people_dict[person] = idx
        idx += 1
    else: # if action == " leave"
        person_gonna_leave = people_dict[person]
        people_stayed[person_gonna_leave] = ""

people_stayed.sort(reverse=True)
for person in people_stayed:
    if person:
        print(person)