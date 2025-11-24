import sys
sys.stdin = open("input.txt", "r")

# python sort() 메서드는 안정정렬 알고리즘으로, 데이터가 입력된 순서를 보장하여,
# 직접 데이터 입력 순서를 정렬 키로 넣어주지 않아도 무방하다.

N = int(input())
registered_array = list()
order_cnt = 0
for _ in range(N):
    order_cnt += 1
    member = input().split()
    member.append(order_cnt)
    registered_array.append(member)

registered_array.sort(key=lambda x:(int(x[0]), x[2]))

for member in registered_array:
    age, name = member[0], member[1]
    print(age, name)