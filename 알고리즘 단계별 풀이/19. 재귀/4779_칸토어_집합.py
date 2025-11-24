import sys
sys.stdin = open("input.txt", "r")

def cantor_function(start, end, array, level):

    if level == 0:
        return

    new_end = start + 3 ** (level - 1) - 1
    new_start = end - 3 ** (level - 1) + 1

    if level == 1:
        array[new_end + 1] = " "
        return

    for i in range(new_end + 1, new_start):
        array[i] = " "

    cantor_function(start, new_end, array, level - 1)
    cantor_function(new_start, end, array, level - 1)

    return

for line in sys.stdin:
    N = int(line.strip())
    cantor_array = ["-"] * (3 ** N)
    cantor_function(0, (3 ** N) - 1, cantor_array, N)

    cantor_result = "".join(cantor_array)
    print(cantor_result)