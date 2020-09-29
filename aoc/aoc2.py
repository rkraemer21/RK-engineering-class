from itertools import islice

hi = open('input2.txt')

pro = []

for line in hi.readlines():
    currentLine = line.split(',')
    for value in currentLine:
        value.replace('\n', '')
        pro.append(int(value))

pro[1] = 12
pro[2] = 2

print(pro)

proIter = iter(pro)

print(proIter)

while proIter == True:
    value = proIter
    if value == 1 or value == 2 or value == 99:
        if value == 1:
            pro[value + 3] = pro[value + 1] + pro[value + 2]
        elif value == 2:
            pro[value + 3] = pro[value + 1] * pro[value + 2]
        elif value == 99:
            continue
        next(proIter, 4)
    else:
        next(proIter)
        

print(pro)
