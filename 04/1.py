total = 0

def by_rows(rows) -> str:
    for row in rows:
        yield row

def by_columns(rows) -> str:
    for column in zip(*rows):
        yield "".join(column)

def by_diagonals(rows) -> str:
    if not rows:
        return
    nr = len(rows)
    nc = len(rows[0])
    # down up diagonals:
    for i in range(nr + nc):
        d = []
        r = min(i, nr-1)
        c = max(0, i-nr + 1)
        while r >= 0 and c < nc:
            d.append(rows[r][c])
            r -= 1
            c += 1
        if len(d) > 0:
            yield "".join(d)
    # up down diagonals:
    for i in range(nr + nc):
        d = []
        r = max(0, nr-1-i)
        c = max(0, i-nr + 1)
        while r < nr and c < nc:
            d.append(rows[r][c])
            r += 1
            c += 1
        if len(d) > 0:
            yield "".join(d)

f = open("input.txt", "r")
rows = f.readlines()


for row in by_diagonals(rows):
    total += row.count("XMAS")
    total += row.count("SAMX")

for row in by_rows(rows):
    total += row.count("XMAS")
    total += row.count("SAMX")

for row in by_columns(rows):
    total += row.count("XMAS")
    total += row.count("SAMX")

print(total)
