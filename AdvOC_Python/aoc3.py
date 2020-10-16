import time

hi = open('input3.txt')

Map = []

for line in hi.readlines():
    h = line.split(',')
    h[-1] = h[-1].strip()
    Map.append(h)

grid = []

for thing in range(0,2):
    x = 0
    y = 0
    grid.append([])
    for phrase in Map[thing]:
        d = phrase[0]
        s = int(phrase[1:])
        if d == 'R':
            x += s
        elif d == 'L':
            x -= s
        elif d == 'U':
            y += s
        elif d == 'D':
            y -= s
#        print(x, '<>', y)
        grid[thing].append([x, y])

    print(x, '<><>', y)

print(grid)

for Set in grid[0]:
    for Set2 in grid[1]:
        if (Set[1] - Set2[1]) == 0 and (Set[0] - Set2[0]) == 0:
            print("BANG!")
        elif (Set[0] - Set2[0]) == 0:
            print("BOOP!")
        elif (Set[1] - Set2[1]) == 0:
            print('BEEP!')
        else:
            print("nope.")

print(time.perf_counter())
