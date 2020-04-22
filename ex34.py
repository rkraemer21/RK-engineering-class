#this is gonna suck
from sys import exit

p = "> "

def goldroom():
    print("This room is full of gold. How much do you take?")
    
    choice = input(p)
    if isinstance(int(choice), int) == True:
        howmuch = int(choice)
    else:
        dead("Man, learn how to type just a number.")

    if howmuch < 50:
        print("Nice, you're not greedy.  You win!")
        exit(0)
    elif choice >= 50:
        dead("You greedy bastard!")

def bearroom():
    print("""There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?""")
    bearmoved = False

    while True:
        choice = input(p)
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bearmoved:
            print("""The bear has moved from the door.
            You can go through it now.""")
            bearmoved = True
        elif choice == "taunt bear" and bearmoved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bearmoved:
            goldroom()
        else:
            print("Type something else, bud")

def cthuluroom():
    print("""Here you see the great evil Cthulu.\nHe, it, whatever stares at you and you go insane.\nDo you flee for your life or eat your head?""")

    choice = input(p)
    
    if "flee" in choice:
        start()
    elif "head" in choice or "eat" in choice:
        dead("Well that was tasty!")
    else:
        cthuluroom()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("""You are in a dark room.\nThere is a door to your right and left.\nWhich one do you take?""")

    choice = input(p)
   
    if "left" in choice:
        bearroom()
    elif "right" in choice:
        cthuluroom()
    else:
        dead("You stumble around the room until you starve.")

start()
