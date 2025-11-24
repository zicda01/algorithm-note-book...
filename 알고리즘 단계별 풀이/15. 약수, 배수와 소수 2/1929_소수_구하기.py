import sys
sys.stdin = open("input.txt", "r")

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        if x % 2 == 0:
            return False
        else:
            divisor = 3
            while (divisor * divisor) <= x:
                if x % divisor == 0:
                    return False
                divisor += 2
            return True

N, M = map(int, input().split())
for num in range(N, M + 1):
    if is_prime(num):
        print(num)