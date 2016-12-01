with open('day1input.txt')as f:
    turns = f.read().split(', ')

position = 0 + 0j
direction = 0 + 1j
visited = [position]
first_twice_dist = False
for turn in turns:
    direction = direction * 1j if turn[0] == 'L' else direction * -1j
    for _ in range(int(turn[1:])):
        position += direction
        visited.append(position)
        if not first_twice_dist and visited.count(position) > 1:
            first_twice_dist = abs(position.real) + abs(position.imag)

total_dist = abs(position.real) + abs(position.imag)
print('Total cab distance: {}'.format(int(total_dist)))
print('First visted twice cab distance: {}'.format(int(first_twice_dist)))
