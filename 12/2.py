f = open("test.txt", "r")
rows = [s.strip() for s in f.readlines()]

visited = set([])

def cont(r, c, dr, dc, d, rows, region):
    s = rows[r][c]
    while True:
        r += dr
        c += dc

        if r < 0 or r >= len(rows) or c < 0 or c >= len(rows[r]):
            return False

        p = (r + d[0], c + d[1])
        if (r, c) in region and (p[0] < 0 or p[0] >= len(rows) or p[1] < 0 or p[1] >= len(rows[p[0]]) or rows[p[0]][p[1]] != s):
            return True

        if rows[r][c] != s:
            return False

def seenL(r, c, rows, region):
    "returns true if left side is visited"
    s = rows[r][c]
    if (r-1, c) in region:
        if c-1 < 0 or (c-1 >= 0 and rows[r-1][c-1] != s):
            return True
    elif cont(r, c, -1, 0, (0, -1), rows, region):
        return True
    if (r+1, c) in region:
        if c-1 < 0 or (c-1 >= 0 and rows[r+1][c-1] != s):
            return True
    elif cont(r, c, 1, 0, (0, -1), rows, region):
        return True
    return False

def seenR(r, c, rows, region):
    "returns true if right side is visited"
    if (r-1, c) in region:
        if c+1 == len(rows[0]) or (c+1 < len(rows[0]) and rows[r-1][c+1] != rows[r][c]):
            return True
    elif cont(r, c, -1, 0, (0, 1), rows, region):
        return True
    if (r+1, c) in region:
        if c+1 == len(rows[0]) or (c+1 < len(rows[0]) and rows[r+1][c+1] != rows[r][c]):
            return True
    elif cont(r, c, 1, 0, (0, 1), rows, region):
        return True
    return False

def seenU(r, c, rows, region):
    "returns true if upper side is visited"
    if (r, c-1) in region:
        if r-1 < 0 or (r-1 >= 0 and rows[r-1][c-1] != rows[r][c]):
            return True
    elif cont(r, c, 0, -1, (-1, 0), rows, region):
        return True
    if (r, c+1) in region:
        if r-1 < 0 or (r-1 >= 0 and rows[r-1][c+1] != rows[r][c]):
            return True
    elif cont(r, c, 0, 1, (-1, 0), rows, region):
        return True
    return False

def seenD(r, c, rows, region):
    "returns true if down side is visited"
    if (r, c-1) in region:
        if r+1 == len(rows) or (r+1 < len(rows) and rows[r+1][c-1] != rows[r][c]):
            return True
    elif cont(r, c, 0, -1, (1, 0), rows, region):
        return True
    if (r, c+1) in region:
        if r+1 == len(rows) or (r+1 < len(rows) and rows[r+1][c+1] != rows[r][c]):
            return True
    elif cont(r, c, 0, 1, (1, 0), rows, region):
        return True
    return False


def get_sides(r, c, rows, region):
    symbol = rows[r][c]
    sides = 0

    next = (r + 1, c)
    if (next[0] < 0 or next[0] >= len(rows) or next[1] < 0 or next[1] >= len(rows[next[0]])) or \
        rows[next[0]][next[1]] != symbol:
        if not seenD(r, c, rows, region):
            sides += 1

    next = (r - 1, c)
    if (next[0] < 0 or next[0] >= len(rows) or next[1] < 0 or next[1] >= len(rows[next[0]])) or \
        rows[next[0]][next[1]] != symbol:
        if not seenU(r, c, rows, region):
            sides += 1

    next = (r, c + 1)
    if (next[0] < 0 or next[0] >= len(rows) or next[1] < 0 or next[1] >= len(rows[next[0]])) or \
        rows[next[0]][next[1]] != symbol:
        if not seenR(r, c, rows, region):
            sides += 1

    next = (r, c - 1)
    if (next[0] < 0 or next[0] >= len(rows) or next[1] < 0 or next[1] >= len(rows[next[0]])) or \
        rows[next[0]][next[1]] != symbol:
        if not seenL(r, c, rows, region):
            sides += 1

    return sides

def walk(r, c, rows, region):
    symbol = rows[r][c]
    visited.add((r, c))
    region.add((r, c))

    area = 1
    sides = get_sides(r, c, rows, region)

    for next in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if next[0] < 0 or next[0] >= len(rows) or next[1] < 0 or next[1] >= len(rows[next[0]]):
            continue
        if next in visited:
            continue

        if rows[next[0]][next[1]] == symbol:
            (da, ds) = walk(next[0], next[1], rows, region)
            area += da
            sides += ds

    return (area, sides)


total = 0
for r in range(len(rows)):
    for c in range(len(rows[r])):
        if (r, c) in visited:
            continue
        a, s = walk(r, c, rows, region=set([]))
        print(f"Symbol: {rows[r][c]}, Area: {a}, Sides: {s}")
        total += a * s

print(total)
