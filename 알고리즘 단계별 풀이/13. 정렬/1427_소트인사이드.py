import sys
sys.stdin = open("input.txt", "r")

# sort() 함수에 reverse=True 인자 전달을 통해 내림차순 정렬을 할 수 있다.

num_array = list(input())
num_array = list(map(int, num_array))
num_array.sort(reverse=True)
num_sorted = "".join(map(str, num_array))
print(num_sorted)