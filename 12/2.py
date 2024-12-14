f = open("input.txt", "r")
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
        if (
            p[0] >= 0
            and p[0] < len(rows)
            and p[1] >= 0
            and p[1] < len(rows[0])
            and rows[p[0]][p[1]] == s
        ):
            return False

        if (r, c) in region:
            if d[0] == -1 and (r - 1 < 0 or rows[r - 1][c] != s):
                return True
            if d[0] == 1 and (r + 1 == len(rows) or rows[r + 1][c] != s):
                return True
            if d[1] == -1 and (c - 1 < 0 or rows[r][c - 1] != s):
                return True
            if d[1] == 1 and (c + 1 == len(rows[r]) or rows[r][c + 1] != s):
                return True
            return False

        if rows[r][c] != s:
            return False


def seenL(r, c, rows, region):
    "returns true if left side is visited"
    s = rows[r][c]
    if (r - 1, c) in region:
        if c - 1 < 0 or (c - 1 >= 0 and rows[r - 1][c - 1] != s):
            return True
    elif cont(r, c, -1, 0, (0, -1), rows, region):
        return True
    if (r + 1, c) in region:
        if c - 1 < 0 or (c - 1 >= 0 and rows[r + 1][c - 1] != s):
            return True
    elif cont(r, c, 1, 0, (0, -1), rows, region):
        return True
    return False


def seenR(r, c, rows, region):
    "returns true if right side is visited"
    if (r - 1, c) in region:
        if c + 1 == len(rows[0]) or (
            c + 1 < len(rows[0]) and rows[r - 1][c + 1] != rows[r][c]
        ):
            return True
    elif cont(r, c, -1, 0, (0, 1), rows, region):
        return True
    if (r + 1, c) in region:
        if c + 1 == len(rows[0]) or (
            c + 1 < len(rows[0]) and rows[r + 1][c + 1] != rows[r][c]
        ):
            return True
    elif cont(r, c, 1, 0, (0, 1), rows, region):
        return True
    return False


def seenU(r, c, rows, region):
    "returns true if upper side is visited"
    if (r, c - 1) in region:
        if r - 1 < 0 or (r - 1 >= 0 and rows[r - 1][c - 1] != rows[r][c]):
            return True
    elif cont(r, c, 0, -1, (-1, 0), rows, region):
        return True
    if (r, c + 1) in region:
        if r - 1 < 0 or (r - 1 >= 0 and rows[r - 1][c + 1] != rows[r][c]):
            return True
    elif cont(r, c, 0, 1, (-1, 0), rows, region):
        return True
    return False


def seenD(r, c, rows, region):
    "returns true if down side is visited"
    if (r, c - 1) in region:
        if r + 1 == len(rows) or (
            r + 1 < len(rows) and rows[r + 1][c - 1] != rows[r][c]
        ):
            return True
    elif cont(r, c, 0, -1, (1, 0), rows, region):
        return True
    if (r, c + 1) in region:
        if r + 1 == len(rows) or (
            r + 1 < len(rows) and rows[r + 1][c + 1] != rows[r][c]
        ):
            return True
    elif cont(r, c, 0, 1, (1, 0), rows, region):
        return True
    return False


def print_region(region, curr, sides):
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if (r, c) in sides:
                print("*", end="")
            elif (r, c) == curr:
                print("C", end="")
            elif (r, c) in region:
                print("X", end="")
            else:
                if rows[r][c] != "O":
                    print(".", end="")
                else:
                    print("O", end="")
        print()
    print(curr)


def get_sides(r, c, rows, region):
    symbol = rows[r][c]
    sides = set([])

    # if r == 4 and c == 7:
    #     print("here")

    next = (r + 1, c)
    if (
        next[0] < 0
        or next[0] >= len(rows)
        or next[1] < 0
        or next[1] >= len(rows[next[0]])
    ) or rows[next[0]][next[1]] != symbol:
        if not seenD(r, c, rows, region):
            sides.add((r + 1, c))

    next = (r - 1, c)
    if (
        next[0] < 0
        or next[0] >= len(rows)
        or next[1] < 0
        or next[1] >= len(rows[next[0]])
    ) or rows[next[0]][next[1]] != symbol:
        if not seenU(r, c, rows, region):
            sides.add((r - 1, c))

    next = (r, c + 1)
    if (
        next[0] < 0
        or next[0] >= len(rows)
        or next[1] < 0
        or next[1] >= len(rows[next[0]])
    ) or rows[next[0]][next[1]] != symbol:
        if not seenR(r, c, rows, region):
            sides.add((r, c + 1))

    next = (r, c - 1)
    if (
        next[0] < 0
        or next[0] >= len(rows)
        or next[1] < 0
        or next[1] >= len(rows[next[0]])
    ) or rows[next[0]][next[1]] != symbol:
        if not seenL(r, c, rows, region):
            sides.add((r, c - 1))

    # if symbol == "O":
    #     print_region(region, (r, c), sides)
    #     print("_________________")
    #     print(f"Sides: {len(sides)}")
    #     print()

    return sides


def walk(r, c, rows, region):
    symbol = rows[r][c]
    visited.add((r, c))
    region.add((r, c))

    area = 1
    sides = len(get_sides(r, c, rows, region))

    for next in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if (
            next[0] < 0
            or next[0] >= len(rows)
            or next[1] < 0
            or next[1] >= len(rows[next[0]])
        ):
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
