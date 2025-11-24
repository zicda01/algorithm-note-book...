from math import comb

N, M = list(map(int, input().split()))
array = list(map(int, input().split()))

prefix_array = [0] * N
prefix_array[0] = array[0]
for i in range(1, N):
    prefix_array[i] = prefix_array[i - 1] + array[i]

cnt = 0
remainder_count_array = [0] * M
for i in range(N):
    remainder = prefix_array[i] % M
    remainder_count_array[remainder] += 1

# for i in range(N):
#     for j in range(i, N):
#         if i == j:
#             target = prefix_array[i]
#         else:
#             target = prefix_array[j] - prefix_array[i]
#         if target % M == 0:
#             cnt += 1

result = remainder_count_array[0]
for i in range(M):
    c = remainder_count_array[i]
    result += comb(c, 2)
print(result)