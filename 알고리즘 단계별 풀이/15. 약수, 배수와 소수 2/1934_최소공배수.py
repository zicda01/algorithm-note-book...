import sys
sys.stdin = open("input.txt","r")

# 유클리드 호제법을 이용해 두 수의 최대 공약수를 구하고,
# 두 수의 곱을 최대 공약수로 나눈 값이 최소 공배수가 된다.

def euclidean(x, y):
    # 더 큰 값이 y라고 가정한다.
    divisor = x
    target_num = y
    while True:
        if not (target_num % divisor):
            break
        temp = target_num
        target_num = divisor
        divisor = temp % divisor

    return divisor

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    if A <= B:
        common_divisor = euclidean(A, B)
    else:
        common_divisor = euclidean(B, A)

    common_multiple = (A * B) // common_divisor
    print(common_multiple)
