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
turning = set()
new_obst = set()

map = []
for l in f.readlines():
    map.append(list(l.strip()))

# find the guard
for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] in directions:
            pos = (r, c)
            direction = map[r][c]
            break

def what_if(pos, direction):
    # returns true if turing at this position will result reaching a position
    # where we have already turned in the same direction.

    assert map[pos[0]][pos[1]] != "#"

    new_obst = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

    assert map[new_obst[0]][new_obst[1]] == "."

    new_dir = rot[direction]
    new_pos = (pos[0], pos[1])
    new_turning = set(turning)

    while True:
        #print_map(map, new_dir, new_pos)
        if (new_pos[0], new_pos[1], new_dir) in new_turning:
            return True
        front = (new_pos[0] + directions[new_dir][0], new_pos[1] + directions[new_dir][1])
        if front[0] < 0 or front[0] >= len(map) or front[1] < 0 or front[1] >= len(map[0]):
            return False
        if map[front[0]][front[1]] == "#" or front == new_obst:
            new_turning.add((new_pos[0], new_pos[1], new_dir))
            new_dir = rot[new_dir]
            continue
        new_pos = front

def print_map(map, direction, pos, obst=set()):
    for r in range(len(map)):
        for c in range(len(map[0])):
            if (r, c) in obst:
                print("O", end="")
            elif (r, c) == pos:
                print(direction, end="")
            else:
                print(map[r][c], end="")
        print()
    print()

while True:
    visited.add(pos)
    front = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])
    if front[0] < 0 or front[0] >= len(map) or front[1] < 0 or front[1] >= len(map[0]):
        break
    if map[front[0]][front[1]] == "#":
        turning.add((pos[0], pos[1], direction))
        direction = rot[direction]
        continue
    if front not in visited and map[front[0]][front[1]] == '.' and what_if(pos, direction):
        if not front in new_obst:
            new_obst.add(front)
            #print_map(map, direction, pos, new_obst)
    pos = front
    assert map[pos[0]][pos[1]] != "#"

print(len(new_obst))
