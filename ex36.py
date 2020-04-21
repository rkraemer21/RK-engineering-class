from sys import exit
import random

p = "\n> "
plchold = 'TBD'
d = '\n---------------------------------------------------------------------------------------\n' # for nicer UI

#variables that save the win status of a fight in each area so you can exit and reenter without it respawning.  hwin currently unused.
gdwin = False
hwin = False

#------------------------------------------------------------
#stats section

armor = 10
weapon = 10
hp = 5000
stats = [hp, armor, weapon]

def status(stats):
    print("\nHP: {} --- ARMOR: {} --- WEAPON: {}\n".format(*stats))

#------------------------------------------------------------

def start():
    status(stats)
    print("There's a light shining over that sand dune.")
    print("You think you know what it is.  Do you walk towards, or away?")

    choice = input(p)
    print(d)

    if "toward" in choice:  #start just takes you to either the hut or the gray desert depending on your choice.
        hut()
    elif "away" in choice:
        graydesert()
    else:
        lostsands() # lost sands is where you go when you say something not recognized.  A little unforgiving but an important element.

#------------------------------------------------------------

def hut():
    status(stats)
    print("You encounter a bad guy.")
    
    dmg = -4
    ehp = 20
    fight(dmg, ehp) # see bottom for fight sequence
    
    if win == True:
        print("You made it into the hut.") # current dead-end, will be expanded
    if win == False:
        start() # this is if you flee the fight, you just go back to start
        
#------------------------------------------------------------
        
def graydesert():
    status(stats)
    print("After mindlessly walking for a while, you find yourself in the middle of a gray desert.")
    print("Something about the place seems... teeming with life, but you don't see anything.")
    print("There is a large rock in front of you. It feels warm and comfortable.  Do you rest on it or keep walking?")

    global gdwin
    global rock
    rock = False

    while True:
        dmg = -10
        ehp = 40
        rwrd = 40

#sitting will activate the rock enemy.  after that, anything will trigger a fight.  If you don't sit, nothing bad happens.

        choice = input(p)
        if (rock == False and gdwin == False) and ("sit" in choice or "rest" in choice):
            print("You sit on the rock and it warms you up.  You rest for a while.")
            print("Time to get going again.  Do you keep going or head back to where you came from?")
            rock = True
        elif rock == True and ("sit" in choice or "rest" in choice):
            print("You sit on the rock again, but this time it goes cold.")
            print("You hop off and look back - the rock is getting up!")
            print("Before you can get away, the Tor slams in front of you.")

            fighthard(dmg, ehp, rwrd)
            if win == True:
                rock = False

            gdwin = win
            print(f"This is a test. win = {win} ---  gdwin = {gdwin}")
        elif rock == True and ("walk" in choice or "keep" in choice):
            print("You walk forward, but something slams in front of you!")
            print("You look behind and see that it is the arm of a giant Tor - the rock you just sat on.")
            fighthard(dmg, ehp, rwrd)

            if win == True:
                rock = False

            gdwin = win
            print(f"This is a test.  win = {win} ---  gdwin = {gdwin}")
        elif (rock == False and gdwin == True) and ("sit" in choice or "rest" in choice):
            print("You sit on the rock again.  Stop being lazy and do something.")
        elif rock == False and ("walk" in choice or "keep" in choice):
            #print("This will go to gray crags")
            #break
            start()
            break
        else:
            if rock == True:
                print("You don't know what you were thinking, but now the rock you sat on is alive!")
                print("The rock attacks you.")
                fighthard(dmg, ehp, rwrd)
                if win == True:
                    rock = False
                gdwin = win
                print(f"This is a test. win = {win} ---  gdwin = {gdwin}")
            else:
                lostsands()
                break

#------------------------------------------------------------

def lostsands():
    status(stats)
    print("After wandering, you realize that was a bad idea anyways.  Now you're lost.\n")
    print("You find yourself in a mysteriously pristine landscape.")
    print("The sand here is tan unlike the rest of the gray desert.")
    print("There seems to be nothing on the horizon, even though you just came from somewhere.")
    print("There's an oasis in front of you, and indecision everywhere else.  Where do you go?")


    lsplchold = "That's odd. Didn't you just come from here? Try something else."
    ls2plchold = "That's a little odd. Doesn't this place look familiar? Try something new."

    prime1 = False
    prime2 = False
    prime3 = False
    prime4 = False

# if you're familiar with the lost woods from Zelda, this is like that.  You need to take a certain path to get out.
# currently it just takes you to the start if you get out, or tells you that it will go to the Oasis, a future spot.

    while True:
        choice = input(p)
        if "oasis" in choice or "forward" in choice:
            if not prime3 == True:
                print(lsplchold)
                prime1 = False
                prime2 = False
            elif prime3 == True:
                #lsoasis()
                print("TBD Oasis")
                break
        elif "north" in choice or "North" in choice:
            if prime2 == False:
                print(lsplchold)
                prime1 = False
            elif prime2 == True:
                print(ls2plchold)
                prime3 = True
        elif "east" in choice or "East" in choice: # start with east, then south, north, then (oasis) or (east > west)
            if prime1 == False:
                print(ls2plchold)
                prime1 = True    
            elif prime1 == True and prime3 == False:
                print(lsplchold)
                prime1 = False
                prime2 = False
            elif prime1 == True and prime3 == True:
                print(ls2plchold)
                prime4 = True
        elif "south" in choice or "South" in choice:
            if prime1 == False:
                print(lsplchold)
            elif prime1 == True:
                print(ls2plchold)
                prime2 = True
        elif "west" in choice or "West" in choice:
            if prime4 == False:
                print(lsplchold)
                prime1 = False
                prime2 = False
                prime3 = False
            elif prime4 == True:
                start()
                break
        else:
            print("The desert must be getting to your head. Think again.")

#------------------------------------------------------------

# fight for easier enemies.  pseudo-randomized damage per hit, in your favor.  You can flee and currently in the hut, the only location in which
#this is used, it will take you back to start.

def fight(dmg, ehp):
    global win
    global weapon

    print(f"The enemy has {ehp} HP.")

    for x in range(1):
        weapon = random.randint(weapon-2, weapon+4)

    choice = input(f"{d}\nHit or flee? > ")

    if "hit" in choice or "Hit" in choice:
        ehp -= weapon # you do damage first
        if ehp <= 0:
            print(f"{d}\nYou beat them.")
            win = True
        else:
            life(dmg) # they do damage second.  see life function below for damage
            fight(dmg, ehp) # then it loops
    elif "flee" in choice or "Flee" in choice:
        print(f"{d}\nYou fled.")
        win = False
  
#------------------------------------------------------------

def fighthard(dmg, ehp, rwrd):
        global win
        global weapon
        for x in range(1):
            weapon = random.randint(weapon-2, weapon+3)  #random damage per hit from you, in your favor.
 
        for x in range(1):
            dmg = random.randint(dmg-5, dmg+5) # random damage per hit from the enemy, in your favor.
        life(dmg) #calls life function, which is how damage is done
 
        choice = input("\nHit or flee? > ")
        if "hit" in choice or "Hit" in choice:
            ehp -= weapon
            if ehp <= 0:
                print("You won.")
                win = True
                if weapon < rwrd:   # see graydesert() for where reward is defined.  You get it if you win and it's higher than current weapon
                   weapon = rwrd
                   print("You looted a stronger weapon.")
            else:
                print("KG - FH") # KG - FH is just a placeholder test thing so i know everything is working
                fighthard(dmg, ehp, rwrd)
        elif "flee" in choice or "Flee" in choice:
            for x in range(1):
                y = random.randint(1, 10) # in a hard fight, small chance of actually fleeing.
            if y == 2 or y == 6:
                print("Got away safely.")
                win = False
            else:
                print("You couldn't get away.")
                fighthard(dmg, ehp, rwrd)
        else:
            print("You hesitated in thought and got hit again.") # no forgiveness.
            fighthard(dmg, ehp, rwrd)
            
#------------------------------------------------------------

def life(dmg):
    global hp
    hp += dmg # damage is passed into fight then into here 
    stats[0] = hp # changes hp
    status(stats) # prints stats

    if hp <= 0:
        print("You died.\n")
        exit(0)

print(d)
start()
