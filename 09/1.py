total = 0

f = open("input.txt", "r", encoding="utf-8")
l = list([int(c) for c in f.read().strip()])


def disk(l) -> int:
    "read disk"
    for i in range(len(l)):
        if i % 2 == 0:
            for j in range(l[i]):
                yield i // 2
        else:
            for j in range(l[i]):
                yield -1

def rdisk(l) -> int:
    "read disc in reverse"
    for i in range(len(l)-1, -1, -1):
        if i % 2 == 0:
            for j in range(l[i]):
                yield i // 2
        else:
            for j in range(l[i]):
                yield -1

def print_disk(l):
    print("".join(["." if i < 0 else str(i) for i in l]))

def defrag(l) -> int:
    "defrag disk"

    busy = 0
    total = 0
    for c in disk(l):
        total += 1
        if c >= 0:
            busy += 1

    # read disk using two heads
    # one reads from the beginning
    # the other reads from the end
    d = disk(l)
    rd = rdisk(l)
    done = 0
    while True:
        b = next(d, None)
        if b is None:
            return
        if b < 0:
            e = -1
            while e < 0:
                e = next(rd, None)
                if e is None:
                    return
            yield e
        else:
            yield b
        done += 1
        if done == busy:
            for i in range(total - busy):
                yield -1
            return

# print_disk(disk(l))
# print_disk(defrag(l))
# print("0099811188827773336446555566..............")

for i, v in enumerate(defrag(l)):
    if v < 0:
        continue
    total += v * i

print(total)
