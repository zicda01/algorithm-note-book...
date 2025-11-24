import sys
sys.stdin = open("input.txt", "r")

# 현재 코드는 딕셔너리를 이용해, 좌표들의 상대 순위를 새롭게 맵핑하는 방식을 쓰고 있으나,
# 좌표들의 위치(인덱스)를 기억해둔 뒤, 오름차순 정렬 이후, 1씩 증가하는 랭크를 직접 부여하는 방식을 사용한다면,
# 배열과 반복문만으로도 풀이가 가능하다.

N = int(input())
address_array = list(map(int, input().split()))

referenced_array = list(set(address_array.copy()))
referenced_array.sort()
dict_for_map = dict()
ref_length = len(referenced_array)
for i in range(ref_length):
    dict_for_map[str(referenced_array[i])] = i

new_array = list()
for j in range(N):
    index = str(address_array[j])
    new_address = dict_for_map[index]
    new_array.append(new_address)
print(*new_array)