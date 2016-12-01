with open('day1input.txt')as f:
    turns = f.read().split(', ')

position = [0, 0]
direction = 1
for turn in turns:
    direction = direction + 1 if turn[0] == 'R' else direction - 1

    facing = direction % 4
    if facing == 1:
        position[0] += int(turn[1:])
    elif facing == 2:
        position[1] += int(turn[1:])
    elif facing == 3:
        position[0] -= int(turn[1:])
    else:
        position[1] -= int(turn[1:])

cab_distance = abs(position[0]) + abs(position[1])
print(cab_distance)
