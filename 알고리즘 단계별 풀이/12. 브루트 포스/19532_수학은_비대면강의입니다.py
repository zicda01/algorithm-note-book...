import sys
sys.stdin = open("input.txt", "r")

'''
ax + by = c
dx + ey = f
'''

# a, b, c, d, e, f = map(int, input().split())
# is_solved = False
#
# for i in range(-999, 1000):
#     for j in range(-999, 1000):
#         x = i
#         y = j
#         if a*x + b*y == c and d*x + e*y == f:
#             print(x, y)
#             is_solved = True
#             break
#     if is_solved:
#         break

# 이상 브루트포스 알고리즘

a, b, c, d, e, f = map(int, input().split())

x = int((c*e - b*f)/(a*e - b*d))
y = int((c*d - a*f)/(b*d - a*e))

print(x, y)