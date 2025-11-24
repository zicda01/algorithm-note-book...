import sys
sys.stdin = open("input.txt", "r")

def fibonacci(number):
    if number != 1 and number != 0:
        return fibonacci(number - 1) + fibonacci(number - 2)
    elif number == 1:
        return 1
    else:
        return 0

N = int(input())

print(fibonacci(N))