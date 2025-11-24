import sys
# sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
array = [0] * N
for i in range(N):
    array[i] = int(sys.stdin.readline())

temp_array = [0] * N

# 병합정렬을 이용한다.

def merge_sort(start, end, arr, temp):
    mid = (start + end) // 2
    if start < end:
        merge_sort(start, mid, arr, temp)
        merge_sort(mid + 1, end, arr, temp)

    merge(start, mid, end, arr, temp)
    return

def merge(start, mid, end, arr, temp):
    for idx in range(start, end + 1):
        temp[idx] = arr[idx]
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        if temp[i] < temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1
    while i <= mid:
        arr[k] = temp[i]
        i += 1
        k += 1
    return

merge_sort(0, N - 1, array, temp_array)

sys.stdout.write('\n'.join(map(str, array)))