import math
total = 0

def safe(a):
    dec = True
    inc = True
    for i in range(len(a)-1):
        d = math.fabs(a[i] - a[i+1])
        if d < 1 or d > 3:
            return False
        if a[i] <= a[i+1]:
            dec = False
        if a[i] >= a[i+1]:
            inc = False
    return dec or inc

f = open("input.txt", "r")
for line in f:
    a = [int(x) for x in line.split()]
    if safe(a):
        total += 1
        continue
    for i in range(len(a)):
        b = [x for (j, x) in enumerate(a) if j != i]
        if safe(b):
            total += 1
            break

print(total)
