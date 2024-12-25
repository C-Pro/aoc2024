f = open("input.txt")
parts = f.read().strip().split("\n\n")

locks = []
keys = []


def parsepin(lock):
    parsed = []
    for c, _ in enumerate(lock[0]):
        h = -1
        for r, _ in enumerate(lock):
            if lock[r][c] == "#":
                h += 1
        parsed.append(h)
    return parsed


for part in parts:
    lines = part.split("\n")
    if lines[0] == "#" * len(lines[0]):
        locks.append(parsepin(lines))
    else:
        keys.append(parsepin(lines))

total = 0
for l in locks:
    for c in keys:
        fits = True
        for p, _ in enumerate(l):
            if l[p] + c[p] > 5:
                fits = False
                break
        if fits:
            total += 1

print(total)
