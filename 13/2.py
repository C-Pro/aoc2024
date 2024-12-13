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
    p[0] += 10000000000000
    p[1] += 10000000000000

    na = (p[0]*b[1] - p[1]*b[0]) / (a[0]*b[1] - a[1]*b[0])
    if na % 1 != 0:
        continue
    nb = (p[0]*a[1] - p[1]*a[0]) / (b[0]*a[1] - b[1]*a[0])
    if nb % 1 != 0:
        continue

    total += na * pa + nb * pb

print(int(total))
