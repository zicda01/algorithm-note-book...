import sys
sys.stdin = open("input.txt", "r")

def recursion(n):

    if n == 0 or n == 1:
        return 1

    return n * recursion(n - 1)

N = int(input())

print(recursion(N))
