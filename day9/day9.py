import re


def add_til_num(lst, num, reps):
    add_me = ""
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if len(add_me) < num:
                add_me += lst[i][j]
                if len(add_me) == num:
                    add_me *= reps
                    add_me += lst[i][j+1:]
                    new_lst = lst[i+1:]
                    return (new_lst, add_me)
    return ([], add_me)


with open('input.txt') as f:
    data = f.read().strip('\n')

output = ""
num = 0
reps = 0
pattern = r'(\(\d+x\d+\))'
a = re.split(pattern, data)[1:]
i = 0
while len(a) > 0:
    if not a:
        break
    m = re.match(r'\(\d+x\d+\)', a[i])
    if m:
        num, reps = a[i].strip('()').split('x')
        a, add_me = add_til_num(a[i+1:], int(num), int(reps))
        i = 0
        output += add_me
    else:
        output += a[i]
        i += 1
print(len(output))
