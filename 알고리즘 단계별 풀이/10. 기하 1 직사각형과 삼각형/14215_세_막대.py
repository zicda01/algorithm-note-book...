import sys
sys.stdin = open("input.txt", "r")

sides = list(map(int, input().split()))
sides = sorted(sides)

a, b, c = sides
if a == b and b == c and a == c:
    print(a + b + c)
else:
    while c >= a + b:
        c -= 1
        if a == b and b == c and a == c:
            print(a + b + c)
            break
    else:
        print(a + b + c)