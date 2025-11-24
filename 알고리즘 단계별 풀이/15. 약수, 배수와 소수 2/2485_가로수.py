import sys
sys.stdin = open("input.txt", "r")

def euclidean(A, B):
    divisor = A
    target = B
    while target % divisor:
        temp = divisor
        divisor = target % divisor
        target = temp
    return divisor

N = int(input())
trees = [0] * N
for i in range(N):
    tree = int(input())
    trees[i] = tree

intervals = [0] * (N - 1)
for j in range(1, N):
    intervals[j - 1] = trees[j] - trees[j - 1]

for k in range(N - 2):
    if k == 0:
        a, b = intervals[0], intervals[1]
        gcd = euclidean(a, b)
    else:
        a, b = gcd, intervals[k + 1]
        gcd = euclidean(a, b)

should_add_cnt = 0
for interval in intervals:
    should_add_cnt += (interval // gcd) - 1
print(should_add_cnt)