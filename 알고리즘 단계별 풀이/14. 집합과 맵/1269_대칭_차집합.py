import sys
sys.stdin = open("input.txt", "r")

# set() 의 symmetric difference() 매서드를 바로 이용해도 될 것 같다.

A, B = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

set_union = set_a | set_b
set_intersaction = set_a & set_b
set_difference = set_union - set_intersaction

print(len(set_difference))

