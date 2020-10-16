h = open("input1.txt")

hi = []
#test = []
#testFuel = 100756

#while testFuel >= 0:
#    testTotal = []
#    testFuel = ((testFuel / 3) // 1) - 2
#    if testFuel > 0:
#        testTotal.append(testFuel)
#    elif testFuel <= 0:
#        pass
#    test.append(sum(testTotal))

#print(test)
#print(sum(test))

for line in h.readlines():
    total = []
    line2 = line.strip("\n")
    fuel = int(line2)
    while fuel >= 2:
        fuel = ((fuel / 3) // 1) - 2
        total.append(fuel)
    hi.append(sum(total))

print(hi)
print(sum(hi))
