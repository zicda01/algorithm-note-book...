import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num_array = list(map(int, input().split()))
operators_count = list(map(int, input().split()))
operators = ["+", "-", "*", "/"]
operator_stack = list()
limit_depth = sum(operators_count)
max_result = float("-inf")
min_result = float("inf")

def operator_function(depth):
    global operator_stack, max_result, min_result

    if depth == limit_depth:
        temp_result = calculate_result(operator_stack)
        max_result = max(max_result, temp_result)
        min_result = min(min_result, temp_result)
        return

    for i in range(4):
        if operators_count[i]:
            operators_count[i] = operators_count[i] - 1
            operator_stack.append(operators[i])
            operator_function(depth + 1)
            operators_count[i] = operators_count[i] + 1
            operator_stack.pop()
        else:
            continue

    return

def calculate_result(result_array_operator):
    result = num_array[0]
    for i in range(limit_depth):
        if result_array_operator[i] == "+":
            result = result + num_array[i + 1]
        elif result_array_operator[i] == "-":
            result = result - num_array[i + 1]
        elif result_array_operator[i] == "*":
            result = result * num_array[i + 1]
        else:
            if result < 0:
                result = (abs(result) // num_array[i + 1]) * (-1)
            else:
                result = result // num_array[i + 1]

    return result

operator_function(0)

print(max_result, min_result)