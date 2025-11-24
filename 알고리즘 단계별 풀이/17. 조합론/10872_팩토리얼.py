import sys
sys.stdin = open("input.txt", "r")

def calculate_factorial(start, result, limit):

    if start == limit:
        return result

    start += 1
    result = result * start

    return calculate_factorial(start, result, limit)

N = int(input())

result = calculate_factorial(0, 1, N)

print(result)