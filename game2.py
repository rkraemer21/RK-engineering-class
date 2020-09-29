from sys import exit
import random
from textwrap import dedent

p = ">> "

hp = 5000
weapon = 10

def status():
    global hp
    global weapon
    print(f" --- HP: {hp} --- WEAPON: {weapon} --- ")

class life(object):
    def hurt(dmg):
        global hp
        hp -= dmg

        if hp <= 0:
            print("YOU DIED")
            exit(0)

    def heal(health):
        global hp
        hp += health
        print(f"You gained {health} health.")

class fight(object):
    def easy(ehp, edmg):
        global weapon
        while True:
            status()
            print(f"Enemy has {ehp} HP.")
            choice = input("Hit or flee? > ")
            edmg = random.randint(edmg - 5, edmg + 3)
            weapon = random.randint(weapon - 2, weapon + 5)
            
            if choice == "hit" or choice == "Hit":
                ehp -= weapon

                if ehp <= 0:
                    print("You won.")
                    win = True
                    break

                life.hurt(edmg)
            elif choice == "flee" or choice == "Flee":
                print("You fled.")
                win = False
                break
            else:
                print("You hesitated. Think more clearly next time.")

        return win

    def hard(ehp, edmg, rwrd):
        global weapon
        while True:
            status()
            print(f"Enemy has {ehp} HP.  This is a strong enemy!")
            choice = input("Hit or flee? > ")
            edmg = random.randint(edmg - 4, edmg + 5)
            weapon = random.randint(weapon - 3, weapon +4)
            life.hurt(edmg)
            status()

            if choice == "hit" or choice == 'Hit':
                ehp -= weapon

                if ehp <= 0:
                    print("You won! You looted a weapon off of the enemy.")
                    if rwrd > weapon:
                        weapon = rwrd
                        print(f"It's stronger than your current one, so you take it. WEAPON: {weapon}")
                    else:
                        print("But it's no stronger than your current one. You leave it.")
                    win = True
                    break
            elif choice == 'flee' or choice == 'Flee':
                odds = random.randint(1,3)
                if odds == 1:
                    print("Got away safely!")
                    win = False
                    break
                elif odds != 3:
                    print("You couldn't get away!")
            else:
                print("You hesitated and got hit again. Think more clearly next time.")

        return win

class scene(object):
    def __init__(self):
        status()

class start(scene):
    def enter(self):
        print(dedent("""
              There's a light shining over there in that sand dune.
              You think you know what it is.  Do you walk towards or away?
              """))

        choice = input(p)
        
        if "toward" in choice:
            hut.enter()
        elif "away" in choice:
            grayDesert.enter()
        else:
            lostSands.enter()

class hut(scene):
    pass

play = start()
play.enter()
