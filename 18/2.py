f = open("input.txt")
nums = [(int(p[1]), int(p[0])) for p in [l.strip().split(",") for l in f.readlines()]]

rows = 71
cols = 71
bytez = 1024

p = (0, 0)
e = (rows-1, cols-1)

m = [["."] * cols for _ in range(rows)]
for n in range(bytez):
    m[nums[n][0]][nums[n][1]] = "#"

dv = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def pm(m):
    for l in m:
        print("".join(l))
    print()

pm(m)


for bytez in range(1024, len(nums)):
    print(f"Trying {bytez}")
    m = [["."] * cols for _ in range(rows)]
    for n in range(bytez):
        m[nums[n][0]][nums[n][1]] = "#"

    unvisited = set()
    for r, l in enumerate(m):
        for c, v in enumerate(l):
            if v == ".":
                unvisited.add((r, c))

    from math import inf
    dists = [[inf for _ in l] for l in m]
    dists[p[0]][p[1]] = 0
    prev = {}

    while True:
        md = inf
        curr = None
        for u in unvisited:
            if dists[u[0]][u[1]] < md:
                md = dists[u[0]][u[1]]
                curr = u
        if md == inf:
            break

        for d in dv:
            cost = dists[curr[0]][curr[1]] + 1
            nr = curr[0] + d[0]
            nc = curr[1] + d[1]
            if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                if m[nr][nc] != "#" and (nr, nc) in unvisited:
                    if dists[nr][nc] == cost:
                        prev.setdefault((nr, nc), []).append(curr)
                    if dists[nr][nc] > cost:
                        prev[(nr, nc)] = [curr]
                        dists[nr][nc] = cost

        unvisited.remove(curr)

    best = dists[e[0]][e[1]]

    if best == inf:
        print(bytez-1, f"{nums[bytez-1][1]}, {nums[bytez-1][0]}")
        break


# for r, l in enumerate(m):
#     for c, v in enumerate(l):
#         if dists[r][c][0] == inf:
#             print("####", end="")
#         else:
#             print("%04d" % dists[r][c][0], end="")
#     print()

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
