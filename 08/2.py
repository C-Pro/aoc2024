total = 0

f = open("input.txt", "r", encoding="utf-8")
m = {}

rows = 0
cols = 0
for r, l in enumerate(f.readlines()):
    cols = 0
    rows +=1
    for c, v in enumerate(l.strip()):
        cols += 1
        if v != ".":
            m.setdefault(v, []).append((r, c))

def gen_nodes(a, b):
    "get antinodes for parir of antennas"
    d = (a[0] - b[0], a[1] - b[1])
    nodes = set([])
    while a[0] >= 0 and a[1] >= 0 and a[0] < rows and a[1] < cols:
        nodes.add(a)
        a = (a[0] + d[0], a[1] + d[1])

    while b[0] >= 0 and b[1] >= 0 and b[0] < rows and b[1] < cols:
        nodes.add(b)
        b = (b[0] - d[0], b[1] - d[1])

    return nodes

antinodes = set([])
for v in m.values():
    for i in range(len(v) -1):
        for j in range(i + 1, len(v)):
            nodes = gen_nodes(v[i], v[j])
            antinodes.update(nodes)

print(len(antinodes))
