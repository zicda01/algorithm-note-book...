# Pseudo Code 는 아래와 같음
# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n
#         for j <- 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

# 첫째 줄에 코드1 의 수행 횟수를 출력한다.
# 둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다.
# 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.

# n = int(input())
# A = [0] * (n + 1)
# def MenOfPassion(arr, N):
#     sum = 0
#     for i in range(1, N + 1):
#         for j in range(1, N + 1):
#             sum = sum + (arr[i] * arr[j])
#     return sum

n = int(input())
print(n**2)
print(2)