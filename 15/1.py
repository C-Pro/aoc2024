f = open(0)
parts = [s.strip() for s in f.read().split("\n\n")]

m = [[s.strip() for s in l] for l in parts[0].split("\n")]


def pm(m):
    for l in m:
        print("".join(l))
    print()


p = None
for r, l in enumerate(m):
    for c, v in enumerate(l):
        if v == "@":
            p = (r, c)
            break
    if p:
        break

moves = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


def move(m, d, p):
    r, c = p
    dr, dc = moves[d]
    has, want = m[r + dr][c + dc], (r + dr, c + dc)
    if has == "#":
        return p
    if has == ".":
        m[r][c], m[r + dr][c + dc] = ".", "@"
        return want
    if has == "O":
        moved = 0
        nr, nc = want[0], want[1]
        while True:
            nr, nc = nr + dr, nc + dc
            if nr < 0 or nr >= len(m) or nc < 0 or nc >= len(m[0]):
                break
            if m[nr][nc] == "#":
                break
            if m[nr][nc] == ".":
                m[r][c], m[r + dr][c + dc], m[nr][nc] = ".", "@", "O"
                return want
        return p


pm(m)
for d in [d for d in parts[1] if d in moves]:
    print(d)
    p = move(m, d, p)
    pm(m)


total = 0
for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] == "O":
            total += r * 100 + c

print(total)
