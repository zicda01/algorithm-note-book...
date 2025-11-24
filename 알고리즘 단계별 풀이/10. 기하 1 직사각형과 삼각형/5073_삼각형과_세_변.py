import sys
sys.stdin = open("input.txt", "r")

while True:
    a, b, c = map(int, input().split())
    if a <= 0 or b <= 0 or c <= 0:
        break

    if a == b and a == c and b == c:
        print("Equilateral")

    elif (a + b + c) > 2 * max(a, b, c):
        if a == b or a == c or b == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")