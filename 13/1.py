import re
total = 0

f = open("input.txt", "r")
m = f.read().strip().split("\n\n")

pa = 3
pb = 1

for mm in m:
    l = mm.split("\n")
    a = list([int(x) for x in re.match(r"Button A: X\+(\d+), Y\+(\d+)", l[0]).groups()])
    b = list([int(x) for x in re.match(r"Button B: X\+(\d+), Y\+(\d+)", l[1]).groups()])
    p = list([int(x) for x in re.match(r"Prize: X=(\d+), Y=(\d+)", l[2]).groups()])

    bp = None
    for na in range(0, 100):
        for nb in range(0, 100):
            if (na * a[0] + nb * b[0], na * a[1] + nb * b[1]) == (p[0], p[1]):
                if bp is None:
                    bp = na * pa + nb * pb
                else:
                    bp = min(bp, na * pa + nb * pb)

    if bp is not None:
        total += bp

print(total)
