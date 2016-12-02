with open('day2input.txt') as f:
    button_steps = [list(x) for x in f.read().splitlines()]

num = 5
nums = []
for step in button_steps:
    for move in step:
        if move == 'U':
            num = num if num in [1, 2, 3] else num - 3
        elif move == 'R':
            num = num if num in [3, 6, 9] else num + 1
        elif move == 'D':
            num = num if num in [7, 8, 9] else num + 3
        else:
            num = num if num in [1, 4, 7] else num - 1
    nums.append(num)
print(nums)
