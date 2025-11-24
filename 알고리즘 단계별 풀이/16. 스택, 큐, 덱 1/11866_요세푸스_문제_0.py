import sys
sys.stdin = open("input.txt", "r")

# 두 개의 list를 이용한 2 stack 전략이 더 나을수도?
# 하나의 deque 자료구조를 이용해서 가장 앞의 요소를 뒤로 보내고, 순서에 해당하는 숫자를 제거하는 방식으로 원형 큐 형태의 요세푸스 순열을 구현 가능.

N, K = list(map(int, input().split()))
queue = list(range(1, N + 1))

top = K - 1
result_array = list()
for _ in range(N):
    while top >= len(queue):
        top = top - len(queue)
    target = queue.pop(top)
    result_array.append(target)
    top += K - 1


josephus_array = ", ".join(map(str, result_array))

sys.stdout.write("<" + josephus_array + ">")