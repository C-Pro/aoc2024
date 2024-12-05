import re
total = 0

f = open("input.txt", "r")
for match in re.findall(r"mul\(([0-9]+),([0-9]+)\)", f.read()):
    total += int(match[0]) * int(match[1])

print(total)
