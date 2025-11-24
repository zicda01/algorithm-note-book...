import sys
sys.stdin = open("input.txt", "r")

# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             for k <- 1 to n
#                 sum <- sum + A[i] × A[j] × A[k]; # 코드1
#     return sum;
# }

# 첫째 줄에 코드1 의 수행 횟수를 출력한다.
# 둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다.
# 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

n = int(input())
# cnt = 0
# A = [0] * (n + 1)
# sum = 0
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         for k in range(1, n + 1):
#             sum = sum + (A[i] * A[j] * A[k])
#             cnt += 1
# result = cnt

print(n**3)
print(2)