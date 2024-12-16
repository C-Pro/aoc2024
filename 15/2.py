f = open(0)
parts = [s.strip() for s in f.read().split("\n\n")]

conv = {"#": "##", ".": "..", "O": "[]", "@": "@."}

m = []
for l in parts[0].split("\n"):
    ll = []
    for c in l:
        ll.append(conv[c])
    m.append(ll)


def pm(m):
    for l in m:
        print("".join(l))
    print()


p = None
for r, l in enumerate(m):
    for c, v in enumerate(l):
        if v == "@":
            p = (r, c)
            break
    if p:
        break

moves = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


def move(m, d, p):
    r, c = p
    dr, dc = moves[d]
    has, want = m[r + dr][c + dc], (r + dr, c + dc)
    if has == "#":
        return p
    if has == ".":
        m[r][c], m[r + dr][c + dc] = ".", "@"
        return want
    if has in ["[", "]"]:
        # horizontal mvmt is similar to pt1
        if dr == 0:
            nr, nc = want[0], want[1]
            while True:
                nr, nc = nr + dr, nc + dc
                if nr < 0 or nr >= len(m) or nc < 0 or nc >= len(m[0]):
                    break
                if m[nr][nc] == "#":
                    break
                if m[nr][nc] == ".":
                    for cc in range(nc, c, -dc):
                        m[r][cc - dc] = m[r][cc]
                    m[r][c] = "."
                    return want
            return p
        else:
            boxes = [(r, c, c + 1)]
            if has == "]":
                boxes = [(r, c - 1, c)]
            boxes = canmovev(m, d, boxes)
            if boxes:
                movev(m, d, boxes)
                return want
            return p


def canmovev(m, d, boxes):
    r, c = p
    dr, _ = moves[d]
    newboxes = []
    for box in boxes:
        br, bc1, bc2 = box
        if m[br+dr][bc1] == "#" or m[br+dr][bc2] == "#":
            return None
        if m[br+dr][bc1] == "[":
            if (br+dr, bc1, bc2) not in newboxes:
                newboxes.append((br+dr, bc1, bc2))
        if m[br+dr][bc1] == "]":
            if (br+dr, bc1-1, bc1) not in newboxes:
                newboxes.append((br+dr, bc1-1, bc1))
        if m[br+dr][bc2] == "[":
            if (br+dr, bc2, bc2+1) not in newboxes:
                newboxes.append((br+dr, bc2, bc2+1))
        if m[br+dr][bc2] == "]":
            if (br+dr, bc2-1, bc2) not in newboxes:
                newboxes.append((br+dr, bc2-1, bc2))
    b = canmovev(m, d, newboxes)
    if b is None:
        return None

    boxes.extend(b)
    return boxes


def movev(m, d, boxes):
    dr, _ = moves[d]
    w = set()
    for box in reversed(boxes):
        br, bc1, bc2 = box
        m[br + dr][bc1], m[br + dr][bc2] = m[br][bc1], m[br][bc2]
        w.add((br + dr, bc1))
        w.add((br + dr, bc2))
    for br, bc1, bc2 in boxes:
        if (br, bc1) not in w:
            m[br][bc1] = "."
        if (br, bc2) not in w:
            m[br][bc2] = "."


pm(m)
for d in [d for d in parts[1] if d in moves]:
    print(d)
    p = move(m, d, p)
    pm(m)


# total = 0
# for r in range(len(m)):
#     for c in range(len(m[0])):
#         if m[r][c] == "O":
#             total += r * 100 + c

# print(total)
