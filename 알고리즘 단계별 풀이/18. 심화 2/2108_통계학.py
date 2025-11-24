import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
array = list()
array_sum = 0
dict_count = dict()
for _ in range(N):
    num = int(sys.stdin.readline())
    array.append(num)
    array_sum += num
    if num in dict_count:
        dict_count[num] += 1
    else:
        dict_count[num] = 0

array.sort()
array_count = list(dict_count.items())
array_count.sort(key=lambda x: (-x[1], x[0]))

if N != 1:
    if array_count[0][1] == array_count[1][1]:
        mode = array_count[1][0]
    else:
        mode = array_count[0][0]
else:
    mode = array_count[0][0]

print(round(array_sum / N))
print(array[N // 2])

print(mode)
print(max(array) - min(array))