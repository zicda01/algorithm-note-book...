import sys
sys.stdin = open("input.txt", "r")

# in 연산자와 set 자료형을 조합하여, 원소가 집합에 포함되는지 빠르게 확인할 수 있다.

N = int(sys.stdin.readline())
my_cards = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
target_cards = list(map(int, sys.stdin.readline().split()))

result = [0] * M
idx = 0
for card in target_cards:
    if card in my_cards:
        result[idx] = 1
    idx += 1

for number in result:
    sys.stdout.write(str(number) + ' ')