N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
half_length = N // 2
team_chosen_first = list()
visited_player = [0] * (N + 1)
min_value = float("inf")

def determine_team(depth, start_index):
    global min_value

    if depth == half_length:
        other_team = determin_other_team()
        value1 = calculate_value(team_chosen_first)
        value2 = calculate_value(other_team)
        min_value = min(abs(value1 - value2), min_value)
        return

    for i in range(start_index, N + 1):
        if visited_player[i]:
            continue
        visited_player[i] = 1
        team_chosen_first.append(i)
        determine_team(depth + 1, i)
        visited_player[i] = 0
        team_chosen_first.pop()

    return

def determin_other_team():
    other_team_array = list()
    for i in range(1, N + 1):
        if visited_player[i]:
            continue
        other_team_array.append(i)

    return other_team_array

def calculate_value(team_array):
    value = 0
    for i in range(half_length - 1):
        for j in range(i + 1, half_length):
            p1 = team_array[i] - 1
            p2 = team_array[j] - 1
            value += matrix[p1][p2] + matrix[p2][p1]

    return value

determine_team(0, 1)

print(min_value)