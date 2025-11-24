import sys
sys.stdin = open("input.txt", "r")

# 소수 검사를 위해 검사 대상이 되는 수와, 인수로 사용되는 자연수는 모두 홀수로 하여 계산을 줄인다.
# 대상이 되는 수의 제곱근 까지만 확인하여 계산을 더 줄일 수 있다.

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        if x % 2 == 0:
            return False
        else:
            factor = 3
            while (factor * factor) <= x:
                if x % factor == 0:
                    return False
                else:
                    factor += 2
            return True

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())

    while True:
        if is_prime(num):
            break
        num += 1
    print(num)