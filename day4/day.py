from collections import Counter
from string import ascii_lowercase

with open('input.txt') as f:
    rooms = f.read().splitlines()

sector_sum = 0
for room in rooms:
    name = room[:-11]
    sector = int(room[-10:-7])
    checksum = room[-6:-1]
    counts = Counter(name.replace('-', ''))
    counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    goodcheck = ''.join([x[0] for x in counts[:5]])
    if goodcheck == checksum:
        sector_sum += sector
        shift = sector % 26
        shifted = ascii_lowercase[shift:] + ascii_lowercase[:shift]
        table = str.maketrans(ascii_lowercase, shifted)
        name = name.translate(table).replace('-', ' ')
        if name == 'northpole object storage':
            print('part 2: ' + str(sector))
print('part 1: ' + str(sector_sum))
