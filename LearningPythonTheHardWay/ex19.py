#defines the function with the arguments cheese and crackers
def cac(cheese, crackers):
    print(f"You have {cheese} cheeses!")
    print(f"You have {crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly.")
cac(20, 30)

print("OR, we can use variables from our script: ")
acheese = 10
acrackers = 50

cac(acheese, acrackers)

print("We can even do math inside too!")
cac(100 / 4, 50 + 2)

print("And we can combine the two: variables and math:")
cac(acheese + 100, acrackers+ 1000)
