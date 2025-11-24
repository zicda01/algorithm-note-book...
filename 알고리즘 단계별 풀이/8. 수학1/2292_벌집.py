import sys
sys.stdin = open("input.txt", "r")

N = int(input())    # 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

initial_num = 1

multiple = 6

cnt = 0
target_num = 1

while True:
    target_num = target_num + (cnt * multiple)
    if N <= target_num:
        print(cnt + 1)
        break
    else:
        cnt += 1