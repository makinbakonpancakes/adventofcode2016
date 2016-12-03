with open('input.txt') as f:
    triangles_1 = [[int(x) for x in line.split()]
                   for line in f.read().splitlines()]

columns = list(zip(*triangles_1))
triangles_2 = []
for col in columns:
    triangles_2.extend([[col[x], col[x+1], col[x+2]]
                        for x in range(0, len(col)-1, 3)])
not_triangles = []
yes_triangles = []
# to switch parts, change to triangles_1
for tri in triangles_2:
    a, b, c = tri[0], tri[1], tri[2]
    if a+b > c and a+c > b and b+c > a:
        yes_triangles.append(tri)
    else:
        not_triangles.append(tri)
print(len(yes_triangles))
print(len(not_triangles))
