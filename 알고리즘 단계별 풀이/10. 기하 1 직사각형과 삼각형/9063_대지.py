import sys
sys.stdin = open("input.txt", "r")

T = int(input())
w_box = list()
h_box = list()
for i in range(T):
    w, h = list(map(int, input().split()))
    w_box.append(w)
    h_box.append(h)

min_w, min_h = min(w_box), min(h_box)
max_w, max_h = max(w_box), max(h_box)

result = (max_w - min_w) * (max_h - min_h)
print(result)