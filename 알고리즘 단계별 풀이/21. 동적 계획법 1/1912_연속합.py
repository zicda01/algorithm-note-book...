N = int(input())
numbers = list(map(int, input().split()))

array = [0] * N
array[0] = numbers[0]
max_serial_sum = array[0]
for i in range(1, N):
    array[i] = max(array[i - 1] + numbers[i], numbers[i])
    if max_serial_sum < array[i]:
        max_serial_sum = array[i]
print(max_serial_sum)
