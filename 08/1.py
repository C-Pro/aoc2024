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
    nodes = [(a[0] + d[0], a[1] + d[1]), (b[0] - d[0], b[1] - d[1])]
    return nodes

def filter_nodes(nodes):
    "filter out of map nodes"
    return [n for n in nodes if n[0] >= 0 and n[1] >= 0 and n[0] < rows and n[1] < cols]

antinodes = set([])
for v in m.values():
    for i in range(len(v) -1):
        for j in range(i + 1, len(v)):
            nodes = filter_nodes(gen_nodes(v[i], v[j]))
            antinodes.update(nodes)

print(len(antinodes))
