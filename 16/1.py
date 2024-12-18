f = open("test.txt")
parts = [s.strip() for s in f.read().split("\n\n")]

m = [[s.strip() for s in l] for l in parts[0].split("\n")]


def pm(m):
    for l in m:
        print("".join(l))
    print()

ds = ['>', 'v', '<', '^']
dv = [(0, 1), (1, 0), (0, -1), (-1, 0)]


p = None
e = None
unvisited = set()
for r, l in enumerate(m):
    for c, v in enumerate(l):
        if v == "S":
            p = (r, c)
        if v == "E":
            e = (r, c)
        if v != "#":
            unvisited.add((r, c))

from math import inf
dists = [[(inf, 0) for _ in l] for l in m]
dists[p[0]][p[1]] = (0, 0)
prev = {}

while True:
    md = inf
    curr = None
    for u in unvisited:
        if dists[u[0]][u[1]][0] < md:
            md = dists[u[0]][u[1]][0]
            curr = u
    if md == inf:
        break
    # two clockwise turns
    for d in range(0, 3):
        cost = dists[curr[0]][curr[1]][0] + 1 + d * 1000
        nd = (dists[curr[0]][curr[1]][1] + d) % 4
        nr = curr[0] + dv[nd][0]
        nc = curr[1] + dv[nd][1]
        if m[nr][nc] != "#" and (nr, nc) in unvisited:
            if dists[nr][nc][0] == cost:
                prev.setdefault((nr, nc), []).append(curr)
            if dists[nr][nc][0] > cost:
                prev[(nr, nc)] = [curr]
                dists[nr][nc] = (cost, nd)
    # one counter clockwise turn
    cost = dists[curr[0]][curr[1]][0] + 1 + 1000
    nd = (dists[curr[0]][curr[1]][1] - 1) % 4
    nr = curr[0] + dv[nd][0]
    nc = curr[1] + dv[nd][1]
    if m[nr][nc] != "#" and (nr, nc) in unvisited:
        if dists[nr][nc][0] == cost:
            prev.setdefault((nr, nc), []).append(curr)
        if dists[nr][nc][0] > cost:
            prev[(nr, nc)] = [curr]
            dists[nr][nc] = (cost, nd)

    unvisited.remove(curr)

best = dists[e[0]][e[1]][0]

# print(best)
# print(prev)
for c in prev:
    if len(prev[c]) > 1:
        print(c, prev[c])
#exit(0)


for r, l in enumerate(m):
    for c, v in enumerate(l):
        if dists[r][c][0] == inf:
            print("####", end="")
        else:
            print("%04d" % dists[r][c][0], end="")
    print()

exit(0)
def pmv(m, spots):
    for r, l in enumerate(m):
        for c, v in enumerate(l):
            if (r, c) in spots:
                print("O", end="")
            else:
                print(v, end="")
        print()
    print()

spots = set([e])
stack = [e]
while True:
    if len(stack) == 0:
        break
    curr = stack.pop()
    for p in prev.get(curr, []):
        spots.add(p)
        stack.append(p)


pmv(m, spots)
print(len(spots))

# for r, l in enumerate(m):
#     for c, v in enumerate(l):
#         if dists[r][c][0] == inf:
#             print("####", end="")
#         else:
#             print("%04d" % dists[r][c][0], end="")
#     print()
# print()
