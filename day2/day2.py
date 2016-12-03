with open('day2input.txt') as f:
    button_steps = [list(x) for x in f.read().splitlines()]


def check_1(pair):
    """Make sure that no abs(number) is greater than 1"""
    return abs(pair[0]) < 2 and abs(pair[1]) < 2


def check_2(pair):
    """Make sure the sum of the (abs) pair doesnt go past 2"""
    return abs(pair[0]) + abs(pair[1]) < 3


keypad_grid_1 = {(-1, 1): 1,
                 (0, 1): 2,
                 (1, 1): 3,
                 (-1, 0): 4,
                 (0, 0): 5,
                 (1, 0): 6,
                 (-1, -1): 7,
                 (0, -1): 8,
                 (1, -1): 9}

keypad_grid_2 = {(0, 2): 1,
                 (-1, 1): 2,
                 (0, 1): 3,
                 (1, 1): 4,
                 (-2, 0): 5,
                 (-1, 0): 6,
                 (0, 0): 7,
                 (1, 0): 8,
                 (2, 0): 9,
                 (-1, -1): 'A',
                 (0, -1): 'B',
                 (1, -1): 'C',
                 (0, -2): 'D'}
num = [0, 0]
keys = []
for step in button_steps:
    for move in step:
        temp_num = [num[0], num[1]]
        if move == 'U':
            temp_num[1] += 1
        elif move == 'R':
            temp_num[0] += 1
        elif move == 'D':
            temp_num[1] -= 1
        else:
            temp_num[0] -= 1
        if check_1(temp_num):
            num = [temp_num[0], temp_num[1]]
    keys.append(keypad_grid_1[tuple(num)])
print(''.join(map(str, keys)))
