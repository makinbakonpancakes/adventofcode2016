with open('day1input.txt')as f:
    turns = f.read().split(',')

position = [0, 0]
positions = []
direction = 1
for turn in turns:
    turn = turn.strip()
    if turn[0] == 'R':
        direction += 1
    if turn[0] == 'L':
        direction -= 1

    facing = direction % 4
    move = int(turn[1:])
    for _ in range(move):
        if facing == 1:
            position[1] += 1
        elif facing == 2:
            position[0] += 1
        elif facing == 3:
            position[1] -= 1
        else:
            position[0] -= 1

        positions.append([position[0], position[1]])
        if (positions.count([position[0], position[1]]) > 1):
            print(abs(position[0]) + abs(position[1]))

cab_distance = abs(position[0]) + abs(position[1])
print(cab_distance)
