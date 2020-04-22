numbers = []

def whilee(x, y, z):
    while x < y:
        print(f"At the top x is {x}.")
        numbers.append(x)

        x += z

        print(f"Numbers now: {numbers}")
        print(f"At the bottom x is {x}.")

whilee(3, 10, 2)

print("The numbers: ")

for num in numbers:
    print(num)
