import sys
sys.stdin = open("input.txt", "r")

a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

# def f(N):
#     return a1 * N + a0
# def g(N):
#     return c * N

def O(N):
    return (a1 - c) * N + a0

if a1 > c:
    print(0)
else:
    if O(n) > 0:
        print(0)
    else:
        print(1)