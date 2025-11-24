import sys
sys.stdin = open("input.txt", "r")

def divide_merge(start, end, array, tempArray):
    if start < end:
        mid = (start + end) // 2
        divide_merge(start, mid, array, tempArray)
        divide_merge(mid + 1, end, array, tempArray)
        merge(start, mid, end, array, tempArray)

    return

def merge(start, mid, end, array, tempArray):
    global recurssion_cnt
    global recurssion_target

    i = start
    j = mid + 1
    k = start

    while i <= mid and j <= end:
        if array[i] <= array[j]:
            tempArray[k] = array[i]
            recurssion_cnt += 1
            if recurssion_cnt == K:
                recurssion_target = tempArray[k]
            i += 1
        else:
            tempArray[k] = array[j]
            recurssion_cnt += 1
            if recurssion_cnt == K:
                recurssion_target = tempArray[k]
            j += 1
        k += 1
    while i <= mid:
        tempArray[k] = array[i]
        recurssion_cnt += 1
        if recurssion_cnt == K:
            recurssion_target = tempArray[k]
        i += 1
        k += 1

    while j <= end:
        tempArray[k] = array[j]
        recurssion_cnt += 1
        if recurssion_cnt == K:
            recurssion_target = tempArray[k]
        j += 1
        k += 1

    for idx in range(start, end + 1):
        array[idx] = tempArray[idx]

    return


N, K = list(map(int, input().split()))
array = list(map(int, input().split()))
temp_array = [0] * N
recurssion_cnt = 0
recurssion_target = -1

divide_merge(0, N - 1, array, temp_array)

print(recurssion_target)
