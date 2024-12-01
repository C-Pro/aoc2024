a = []
b = {}

f = open("test.txt", "r")
for line in f:
    l, r = line.split()
    a.append(l)
    if r not in b:
        b[r] = 1
    else:
        b[r] += 1

total = 0
for n in a:
    total += int(n) * b.get(n, 0)

print(total)
