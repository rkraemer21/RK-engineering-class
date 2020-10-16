h = open("input1.txt")

hi = []

print(((1969 / 3) // 1) - 2)

for line in h.readlines():
    line2 = line.strip("\n")
    line3 = int(line2)
    hi.append(((line3 / 3) // 1) - 2)

print(sum(hi))
