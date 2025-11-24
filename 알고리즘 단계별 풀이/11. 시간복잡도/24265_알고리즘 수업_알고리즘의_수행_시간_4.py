import sys
sys.stdin = open("input.txt", "r")

# Pseudo Code 는 아래와 같음
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# 첫째 줄에 코드1 의 수행 횟수를 출력한다.
# 둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다.
# 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

n = int(input())
# cnt = 0
# A = [0] * (n + 1)
# sum = 0
# for i in range(1, n):
#     for j in range(i + 1, n + 1):
#         sum = sum + (A[i] * A[j])
#         cnt += 1
# result = cnt


result = int((n**2)/2 - n/2)

print(result)
print(2)