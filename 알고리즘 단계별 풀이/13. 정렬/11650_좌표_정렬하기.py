# lambda 문법을 이용한다.

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
array.sort(key=lambda x: (x[0], x[1]))

for data in array:
    print(*data)