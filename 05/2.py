total = 0
pages = set()
rules = {}
updates = []


f = open("input.txt", "r")
first = True
for row in f.readlines():
    if row.strip() == "":
        first = False
        continue

    if first:
        a, b = row.strip().split("|")
        if a not in rules:
            rules[a] = set([])
        rules[a].add(b)
        pages.add(a)
        pages.add(b)
    else:
        updates.append(row.strip().split(","))

pages = list(pages)


def below(a, consider):
    if a not in rules:
        return
    stack = [s for s in rules[a] if s in consider]
    while stack:
        b = stack.pop()
        yield b
        stack.extend([s for s in rules.get(b, []) if s in consider])
        #print(b)

for u in updates:
    rlz = {}
    for r in u:
        rlz[r] = set(below(r, set(u)))

    u_pages = u[:]
    for i in range(len(u_pages)):
        for j in range(i, len(u_pages)):
            if u_pages[i] in rlz and u_pages[j] in rlz[u_pages[i]]:
                u_pages[i], u_pages[j] = u_pages[j], u_pages[i]
    u_pages.reverse()
    weights = {p: i for i, p in enumerate(u_pages)}

    sorted_u = sorted(u, key=lambda x: weights[x])
    if sorted_u != u:
        total += int(sorted_u[len(sorted_u)//2])

print(total)
