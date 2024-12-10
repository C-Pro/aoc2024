total = 0

f = open("input.txt", "r", encoding="utf-8")
l = list([int(c) for c in f.read().strip()])

def disk(l) -> int:
    "read disk"
    c = 0
    for i in range(len(l)):
        if i % 2 == 0:
            files.append((c, l[i]))
            c += l[i]
            for j in range(l[i]):
                yield i // 2
        else:
            free.append((c, l[i]))
            c += l[i]
            for j in range(l[i]):
                yield -1


def print_disk(l):
    print("".join(["." if i < 0 else str(i) for i in l]))

files = []
free = []
disk = list(disk(l))

for i in range(len(files)-1, 0, -1):
    for idx, j in enumerate(free):
        if j[0] > files[i][0]:
            break
        if j[1] >= files[i][1]:
            for l in range(j[0], j[0] + files[i][1]):
                disk[l] = i
            for l in range(files[i][0], files[i][0] + files[i][1]):
                disk[l] = -1
            free[idx] = (free[idx][0] + files[i][1], free[idx][1] - files[i][1])
            break

# print_disk(disk)
# print("00992111777.44.333....5555.6666.....8888..")

total = 0
for i, v in enumerate(disk):
    if v < 0:
        continue
    total += v * i

print(total)
