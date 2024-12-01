a = []
b = []

f = open("input.txt", "r")
for line in f:
    l, r = line.split()
    a.append(l)
    b.append(r)

total = 0
a.sort()
b.sort()
for i in range(len(a)):
    d = int(b[i]) - int(a[i])
    if d < 0:
        d = -d
    total += d

print(total)
