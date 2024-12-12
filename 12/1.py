f = open("input.txt", "r")
rows = [s.strip() for s in f.readlines()]

visited = set([])

def get_perimeter(r, c, rows):
    symbol = rows[r][c]
    perimeter = 0

    for next in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if  (next[0] < 0 or next[0] >= len(rows) or next[1] < 0 or next[1] >= len(rows[next[0]])) or \
            rows[next[0]][next[1]] != symbol:
            perimeter += 1

    return perimeter

def walk(r, c, rows):
    symbol = rows[r][c]
    visited.add((r, c))

    area = 1
    perimeter = get_perimeter(r, c, rows)

    for next in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if next[0] < 0 or next[0] >= len(rows) or next[1] < 0 or next[1] >= len(rows[next[0]]):
            continue
        if next in visited:
            continue

        if rows[next[0]][next[1]] == symbol:
            (da, dp) = walk(next[0], next[1], rows)
            area += da
            perimeter += dp

    return (area, perimeter)


total = 0
for r in range(len(rows)):
    for c in range(len(rows[r])):
        if (r, c) in visited:
            continue
        a, p = walk(r, c, rows)
        total += a * p

print(total)
