# 거스름돈의 액수가 주어지면 리암이 줘야할,
# 쿼터(Quarter, $0.25)의 개수,
# 다임(Dime, $0.10)의 개수,
# 니켈(Nickel, $0.05)의 개수,
# 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오.
# 거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다.
# 예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    money = int(input())
    remainder = 0

    change_type = [25, 10, 5, 1]
    # quarter, dime, nickel, penny = change_type

    change_box = list()
    for change in change_type:
        temp = money // change
        remainder = money % change
        change_box.append(temp)

        money = remainder

    print(*change_box)