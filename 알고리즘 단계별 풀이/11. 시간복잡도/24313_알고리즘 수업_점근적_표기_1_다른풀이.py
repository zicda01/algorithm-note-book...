import sys
sys.stdin = open("input.txt", "r")

a1, a0 = map(int, input().split())
c = int(input()) # c 는 100 이하의 양의 정수
n0 = int(input()) # n 은 100 이하의 양의 정수

def f(N):
    return a1 * N + a0
def g(N):
    return c * N

is_bounded = True
for n in range(n0, 101):
    if f(n) - g(n) > 0:
        is_bounded = False
        break
    else:
        continue

if is_bounded:
    print(1)
else:
    print(0)