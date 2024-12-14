import re

w = 101
h = 103
s = 100

q = [0] * 4


def qadd(r, c):
    if r < h // 2 and c < w // 2:
        q[0] += 1
        return
    if r < h // 2 and c > w // 2:
        q[1] += 1
        return
    if r > h // 2 and c < w // 2:
        q[2] += 1
        return
    if r > h // 2 and c > w // 2:
        q[3] += 1
    return


brd = [[0] * w for i in range(h)]

f = open("input.txt", "r")
bots = {}
for l in f.readlines():
    c, r, vc, vr = (int(s) for s in re.findall(r"(-?\d+)", l))
    b = bots.get((r, c), set([]))
    b.add((vr, vc))
    bots[(r, c)] = b

    sr = (r + vr * s) % h
    sc = (c + vc * s) % w
    qadd(sr, sc)
    brd[sr][sc] += 1

for r in range(h):
    for c in range(w):
        if r == h // 2 or c == w // 2:
            print(" ", end=" ")
        elif brd[r][c] > 0:
            print(brd[r][c], end=" ")
        else:
            print(".", end=" ")
    print()

total = 1
for t in q:
    total *= t
print(total)
