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


def part_1(data):
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
    return len(output)


def wat(data, num=0, reps=0, extra="", totals=[]):
    while len(data) > 0:
        pattern = r'\((\d+)x(\d+)\)(.+)'
        m = re.match(pattern, data)
        if m:
            num = m.group(1)
            reps = m.group(2)
            data = m.group(3)
            totals.append(wat(data, num, reps))
        else:
            return [num * reps]


def part_2(data):
    output = 0
    bruh = []
    pattern = r'\((\d+)x(\d+)\)(.+)'
    pattern2 = r'(.+)\(\d+x\d+\)'
    while data:
        m = re.match(pattern, data)
        if m:
            rest = m.group(3)
            diff = len(data) - len(rest)
            bruh = [[x[0] - diff, x[1], x[2]] for x in bruh]
            data = rest
            num = int(m.group(1))
            reps = int(m.group(2))
            bruh.append([num, reps, 0])
        else:
            if len(bruh) == 0:
                print(bruh)
                m = re.match(pattern2, data)
                output += len(m.group(1))
                data = data[len(m.group(1)):]
            else:
                num, reps, _ = bruh[-1]
                data = data[num:]
                bruh = [[x[0] - num, x[1], x[2]] for x in bruh]
                bruh[-1][2] = num
                while len(bruh) > 0 and bruh[-1][0] == 0:
                    if len(bruh) > 1:
                        _, reps, char_cnt = bruh[-1]
                        bruh[-2] = [bruh[-2][0],
                                    bruh[-2][1],
                                    bruh[-2][2] + char_cnt * reps]
                        bruh = bruh[:-1]
                    else:
                        output += bruh[0][2] * bruh[0][1]
                        bruh = bruh[:-1]
    # 707943143662 too high
    # 384727420 too low
    # 10931789799
    return(output)


with open('input.txt') as f:
    data = f.read().strip('\n')

print(part_1(data))
print(part_2(data))
