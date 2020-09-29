from sys import exit
import random

#hp = 10
#weapon = 10

def status():
    global hp
    global weapon
    print(f" --- HP: {hp} --- WEAPON: {weapon} --- ")

class life(object):
    def __init__(self):
        global hp

    def hurt(dmg):
        global hp
        hp -= dmg

        if hp <= 0:
            print("YOU DIED")
            #exit(0)

    def heal(health):
        global hp
        hp += health
        print(f"You gained {health} health.")

class fight(life):
    def __init__(self):
        global weapon
        self.life = life()

    def easy(self, ehp, edmg):
        while True:
            status()
            print(f"Enemy has {ehp} HP.")
            choice = input("Hit or flee? > ")
            
            if choice == "hit" or choice == "Hit":
                ehp -= weapon

                if ehp <= 0:
                    print("You won.")
                    win = True
                    break

                self.life.hurt(edmg)
            elif choice == "flee" or choice == "Flee":
                print("You fled.")
                win = False
                break
            else:
                print("You hesitated. Think more clearly next time.")

        return win

    def hard(self, ehp, edmg, rwrd):
        while True:
            print(f"Enemy has {ehp} HP.  This is a strong enemy!")
            choice = input("Hit or flee? > ")
            self.life.hurt(edmg)
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
                odds = random.randint(1,4)
                if odds == 3:
                    print("Got away safely!")
                    win = False
                    break
                elif odds != 3:
                    print("You couldn't get away!")
            else:
                print("You hesitated and got hit again. Think more clearly next time.")

            return win
