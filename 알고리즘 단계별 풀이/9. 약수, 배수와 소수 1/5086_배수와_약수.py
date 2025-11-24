import sys
sys.stdin = open("input.txt", "r")

# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.

# 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if B % A == 0:
        print("factor")
    elif A % B == 0:
        print("multiple")
    else:
        print("neither")