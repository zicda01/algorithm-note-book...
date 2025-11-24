import sys
sys.stdin = open("input.txt", "r")

'''
접근 방법이 잘못 되었음.
현재 판에서 어떤 색깔을 칠해야 최소한의 색깔로 검흰이 번갈아 등장하는 board를 만들 수 있는지가 아니라,
주어진 판을 8*8 형태로 자른 뒤 거기서 몇 칸을 칠해서 만들 수 있는 체스판 중에,
최소의 칸판 칠할 수 있는 경우를 구하는 것이므로,
기준점으로 부터 8*8칸의 체스판을 모두 검사하는 로직을 만들어야함.
외부를 이중 반복문을 돌리고, 내부에 8*8칸을 검사하는 함수를 실행하는, 브루트포스 알고리즘을 만들어야 할 것 같음.

검사 시작점이 흰색인지, 검은색인지를 기준으로 함수 분기 만들어서 패턴 검사하기
단순히 돌 개수를 세서 결과를 내는 시도는 안 되는 것 같다.

'''

def check_start_w(R, C):
    cnt = 0
    for i in range(8):
        for j in range(8):
            stone = board[R + i][C + j]
            if i % 2 == 0:
                if j % 2 == 0:
                    if stone != "W":
                        cnt += 1
                else:
                    if stone != "B":
                        cnt += 1
            else:
                if j % 2 == 0:
                    if stone != "B":
                        cnt += 1
                else:
                    if stone != "W":
                        cnt += 1
    return cnt

def check_start_b(R, C):
    cnt = 0
    for i in range(8):
        for j in range(8):
            stone = board[R + i][C + j]
            if i % 2 == 0:
                if j % 2 == 0:
                    if stone != "B":
                        cnt += 1
                else:
                    if stone != "W":
                        cnt += 1
            else:
                if j % 2 == 0:
                    if stone != "W":
                        cnt += 1
                else:
                    if stone != "B":
                        cnt += 1
    return cnt


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

min_result = 64
for r in range(N + 1 - 8):
    for c in range(M + 1 - 8):
        case1 = check_start_w(r, c)
        case2 = check_start_b(r, c)

        if case1 >= case2:
            temp_result = case2
        else:
            temp_result = case1

        if min_result > temp_result:
            min_result = temp_result

print(min_result)
