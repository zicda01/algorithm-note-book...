import sys
sys.stdin = open("input.txt", "r")

limit_range = 1000000
prime_list = [True] * (limit_range + 1)
prime_list[0] = prime_list[1] = False
for i in range(2, int(limit_range ** 0.5) + 1):
    if prime_list[i]:
        for j in range(i ** 2, limit_range + 1, i):
            prime_list[j] = False
N = int(input())
for _ in range(N):
    target = int(input())
    cnt = 0
    visited_set = set()
    for k in range(2, target + 1):
        if prime_list[k] and not(k in visited_set):
            opposite = target - k
            if prime_list[opposite]:
                cnt += 1
                visited_set.add(k)
                visited_set.add(opposite)
    print(cnt)

# 집합을 통해 중복 검사를 하지 않고,
# 순회를 target number의 반만큼만 돌아서 해결하면,
# 시간 복잡도도 줄어들고, 조건도 간단해져, 논리가 더 명확해진다.