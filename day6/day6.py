from collections import Counter

with open('input.txt') as f:
    lines = f.read().splitlines()

columns = list(zip(*lines))
word = [Counter(col).most_common(1)[0][0] for col in columns]
word2 = [sorted(Counter(col).items(), key=lambda x: (x[1], x[0]))[0][0]
         for col in columns]
print('Part 1: ' + ''.join(word))
print('Part 2: ' + ''.join(word2))
