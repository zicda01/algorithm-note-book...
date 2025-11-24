import sys
sys.stdin = open("input.txt", "r")

N = int(input())
my_cards = list(map(int, input().split()))
M = int(input())
target_cards = list(map(int, input().split()))

cards_dict = dict()
for card in target_cards:
    cards_dict[card] = 0

target_cards_set = set(target_cards)
for card in my_cards:
    if card in target_cards_set:
        cards_dict[card] += 1

result_array = list()
for card in target_cards:
    result_array.append(cards_dict[card])

print(*result_array)