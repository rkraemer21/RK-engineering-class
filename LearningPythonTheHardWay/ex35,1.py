from sys import argv

script, dmg = argv

hp = 10

dmg = int(dmg)

def hi(dmg2):
    global hp
    hp -= dmg2

    if hp<= 0:
        print("You died.")
        exit(0)
    else:
        print("you lived.")

hi(dmg)

print(hp)

if hp <= 0:
    print("You died.")
    exit(0)
else:
    print("you lived.")
