f = open("input.txt", "r", encoding="utf-8")
m = []
for line in f.readlines():
    m.append([int(c) for c in line.strip()])

def dfs(r, c, p, m, visited):
    if r < 0 or r >= len(m) or c < 0 or c >= len(m[0]):
        return 0
    if m[r][c] != p + 1:
        return 0
    #if (r,c) in visited:
    #    return 0
    if m[r][c] == 9:
        visited.add((r, c))
        return 1
    s = dfs(r-1, c, m[r][c], m, visited)
    s+= dfs(r+1, c, m[r][c], m, visited)
    s+= dfs(r, c-1, m[r][c], m, visited)
    s+= dfs(r, c+1, m[r][c], m, visited)
    return s

total = 0
for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] == 0:
            total += dfs(r, c, -1, m, set([]))

print(total)
