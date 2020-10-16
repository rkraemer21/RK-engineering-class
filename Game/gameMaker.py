x = input("What would you like your game to be called? > "); x += '.py'

xHandle = open(x, 'x')

areaNum = int(input("How many areas do you want there to be? > "))

areas = []
for x in range(1, areaNum + 1):
    yName = input(f"What would you like to call area {x}? > ")
    y = []
    y.append(yName)
    areas.append(y)

for item in areas[0:]:
    areaComp = int(input(f"How many possible actions do you want in {item}? > "))
    for x in range(1, areaComp + 1):
        #areas[item].append = input("What do you want it to say?")
        print(item)

print(globals())
print(areas)

#xHandle = x.close()
