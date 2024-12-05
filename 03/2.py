import re

total = 0
do = True

re_mul_parse = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
re_all = re.compile(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))")


f = open("input.txt", "r")
s = f.read()

while len(s) > 0:
    match = re_all.search(s)
    if not match:
        ## no matches left
        break
    if match.group(1):
        m = re_mul_parse.match(match.group(1))
        s = s[match.end():]
        if not do:
            continue
        total += int(m.group(1)) * int(m.group(2))
    elif match.group(2):
        s = s[match.end():]
        do = True
    elif match.group(3):
        s = s[match.end():]
        do = False

print(total)
