import re

w = 101
h = 103


f = open("input.txt", "r")
bots = []
for l in f.readlines():
    c, r, vc, vr = (int(s) for s in re.findall(r"(-?\d+)", l))
    bots.append((r, c, vr, vc))


for s in range(1, 1000000):
    brd = [[0] * w for i in range(h)]
    for b in bots:
        r, c, vr, vc = b
        sr = (r + vr * s) % h
        sc = (c + vc * s) % w
        brd[sr][sc] += 1

    maxcont = 0
    for r in range(h):
        cont = 0
        for c in range(w):
            if cont > maxcont:
                maxcont = cont
            if brd[r][c] > 0:
                cont += 1
            else:
                cont = 0
    if maxcont < 10:
        continue

    print(s)

    for r in range(h):
        for c in range(w):
            if brd[r][c] > 0:
                print(brd[r][c], end=" ")
            else:
                print(".", end=" ")
        print()
