import re


with open('input.txt') as f:
    data = f.read()

output = ""
pattern = r'\((\d+x\d+)\)'
a = re.split(pattern, data)
a = a[1:]
for i in range(0, len(a), 2):
    num, reps = a[i].split('x')
    output += a[i+1][:int(num)] * int(reps) + a[i+1][int(num):]
print(len(output))
