from math import inf
from multiprocessing import Pool
from functools import partial

dv = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def pm(m, extra={}):
    for r, l in enumerate(m):
        for c, v in enumerate(l):
            if (r, c) in extra:
                print(extra[(r, c)], end="")
            else:
                print(v, end="")
        print()
    print()

#pm(m)

def dji(m, p, e):
    unvisited = set([e])
    for r, l in enumerate(m):
        for c, v in enumerate(l):
            if v != "#":
                unvisited.add((r, c))


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

    return dists

def dji2(m, p, e, cheat, limit=0, od=[]):
    rows = len(m)
    cols = len(m[0])
    unvisited = set([e])
    cost = od[p[0]][p[1]]
    for r, l in enumerate(m):
        for c, v in enumerate(l):
            if od[r][c] < cost:
                continue
            if v != "#":
                unvisited.add((r, c))
    for c in cheat:
        unvisited.add(c)


    dists = [[inf for _ in l] for l in m]
    dists[p[0]][p[1]] = 0

    while True:
        md = inf
        curr = None
        for u in unvisited:
            if dists[u[0]][u[1]] < md:
                md = dists[u[0]][u[1]]
                curr = u
        if md == inf:
            break

        if md > limit:
            return inf

        for d in dv:
            cost = dists[curr[0]][curr[1]] + 1
            nr = curr[0] + d[0]
            nc = curr[1] + d[1]
            if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                if (nr, nc) in unvisited:
                    if dists[nr][nc] > cost:
                        dists[nr][nc] = cost

        unvisited.remove(curr)

    return dists[e[0]][e[1]]

def check_candidate(candidate, m, start, end, best, od):
    rows = len(m)
    cols = len(m[0])
    cheats = {}
    for d in dv:
        cheat1 = (candidate[0]+d[0], candidate[1]+d[1])
        if cheat1[0] <= 0 or cheat1[0] >= rows-1 or cheat1[1] <= 0 or cheat1[1] >= cols-1:
            continue
        if m[cheat1[0]][cheat1[1]] != "#":
            continue

        cheat2 = (cheat1[0]+d[0], cheat1[1]+d[1])
        if cheat2[0] <= 0 or cheat2[0] >= rows-1 or cheat2[1] <= 0 or cheat2[1] >= cols-1:
            continue
        if m[cheat2[0]][cheat2[1]] == "#":
            continue

        # don't go back
        if od[cheat2[0]][cheat2[1]] < candidate[2]:
            continue

        dist = dji2(m, cheat2, end, [cheat1, cheat2], best - candidate[2], od)
        if dist < inf:
            saved = best - (candidate[2]+2+dist)
            if saved < 1:
                continue

            if saved not in cheats:
                cheats[saved] = 1
            else:
                cheats[saved] += 1

    return cheats

if __name__ == "__main__":
    f = open("input.txt")
    m = [list(l.strip()) for l in f.readlines()]

    rows = len(m)
    cols = len(m[0])
    maxlen = 100

    start = None
    end = None
    for r, l in enumerate(m):
        for c, v in enumerate(l):
            if v == "S":
                start = (r, c)
            if v == "E":
                end = (r, c)

    dists = dji(m, start, end)
    best = dists[end[0]][end[1]]
    print(f"Best path without cheats is {best} picoseconds long")

    candidates = []
    for r, l in enumerate(dists):
        for c, v in enumerate(l):
            if v < best - maxlen:
                candidates.append((r, c, v))


    pool = Pool(10)
    fn = partial(check_candidate, m=m, start=start, end=end, best=best, od=dists)
    res = pool.map(fn, candidates)
    cheats = {}
    for r in res:
        for k, v in r.items():
            if k not in cheats:
                cheats[k] = v
            else:
                cheats[k] += v

    total=0
    items = sorted(cheats.items(), key=lambda x: x[0])
    for k, v in items:
        if k >= maxlen:
            total += v
        if v > 1:
            print(f"There are {v} cheats that save {k} picoseconds")
        else:
            print(f"There is {v} cheat that saves {k} picoseconds")

    print(total)
