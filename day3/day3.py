with open('input.txt') as f:
    triangles_1 = [[int(x) for x in line.split()]
                   for line in f.read().splitlines()]

columns = list(zip(*triangles_1))
triangles_2 = []
for col in columns:
    triangles_2.extend([[col[x], col[x+1], col[x+2]]
                        for x in range(0, len(col)-1, 3)])


def triangle_palooza(triangles):
    yes_triangles = []
    for tri in triangles:
        a, b, c = tri[0], tri[1], tri[2]
        if a+b > c and a+c > b and b+c > a:
            yes_triangles.append(tri)
    return len(yes_triangles)


print(triangle_palooza(triangles_1))
print(triangle_palooza(triangles_2))
