import sys

S = sys.stdin.readline().strip()
tc = int(sys.stdin.readline())
prefix_array = [[0] * len(S) for _ in range(26)]
check_duplicate = set()
for i in range(len(S)):
    target = S[i]
    if target in check_duplicate:
        continue
    check_duplicate.add(target)
    target_count = 0
    turn = ord(target) - ord('a')
    for j in range(len(S)):
        if target == S[j]:
            target_count += 1
        prefix_array[turn][j] = target_count

for _ in range(tc):
    command = list(sys.stdin.readline().split())
    new_target = ord(command[0]) - ord('a')
    l, r = int(command[1]), int(command[2])
    if l >= 1 and r >= 1:
        result = prefix_array[new_target][r] - prefix_array[new_target][l - 1]
    else:
        result = prefix_array[new_target][r]
    sys.stdout.write(str(result) + '\n')