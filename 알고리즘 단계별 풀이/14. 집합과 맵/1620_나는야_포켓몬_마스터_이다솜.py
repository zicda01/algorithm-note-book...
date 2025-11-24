import sys
sys.stdin = open("input.txt", "r")

# isdigit() 메서드를 사용해서 str 데이터가 정수인지 판단할 수 있으나,
# 일반적으로는 try-except 을 이용한 예외처리 문법을 쓰는 게 더 안전하고 강력하다.
# 딕셔너리 자료형을 이용해 빠르게 탐색한다.

N, q = map(int, sys.stdin.readline().split())
poke_dict = dict()
poke_dict_for_key = dict()
idx = 1
for _ in range(N):
    data = sys.stdin.readline().split()[0]
    poke_dict[str(idx)] = data
    poke_dict_for_key[data] = str(idx)
    idx += 1

for _ in range(q):
    command = sys.stdin.readline().split()[0]
    if command.isdigit():
        result = poke_dict[command]

    else:
        result = poke_dict_for_key[command]
    sys.stdout.write(result + '\n')