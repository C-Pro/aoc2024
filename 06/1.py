f = open("input.txt", "r")

direction = ""
pos = (0, 0)
directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

rot = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

visited = set()

map = []
for l in f.readlines():
    map.append(list(l.strip()))

# find the guard
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] in directions:
            pos = (r, c)
            direction = map[r][c]
            map[r][c] = "."
            break

while True:
    visited.add(pos)
    front = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
    if front[0] < 0 or front[0] >= len(map) or front[1] < 0 or front[1] >= len(map[0]):
        break
    if map[front[0]][front[1]] == "#":
        direction = rot[direction]
        continue
    pos = front

print(len(visited))
