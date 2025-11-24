import sys
sys.stdin = open("input.txt", "r")

N = int(input())
is_queue_or_stack = list(map(int, input().split()))
queuestack = list(map(int, input().split()))
M = int(input())
array_appended = list(map(int, input().split()))

q_cnt = 0
q_array = list()
for i in range(N - 1, -1, -1):
    if not is_queue_or_stack[i]:
        q_cnt += 1
        q_array.append(queuestack[i])

if M > q_cnt:
    for j in range(q_cnt):
        print(q_array[j], end=" ")
    for k in range(M - q_cnt):
        print(array_appended[k], end=" ")

else:
    for j in range(M):
        print(q_array[j], end=" ")
