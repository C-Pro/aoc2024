import re

total = 0

f = open("input.txt", "r")
a = f.readlines()

def is_x_mas(r, c) -> bool:
    d1 = "".join([a[r-1][c-1], a[r][c], a[r+1][c+1]])
    d2 = "".join([a[r-1][c+1], a[r][c], a[r+1][c-1]])
    return (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM")


for r in range(1, len(a) - 1):
    for c in range(1, len(a[0]) - 1):
        if a[r][c] != "A":
            continue
        if is_x_mas(r, c):
            total += 1

print(total)
