numbers = []

def whilee(x, y, z):
    while x < y:
        for x in range(x, y, z):
            print(f"At the top x is {x}.")
            numbers.append(x)

            x += z

            print(f"Numbers now: {numbers}")
            print(f"At the bottom x is {x}.")

whilee(int(input()), int(input()), int(input()))

print("The numbers: ")

for num in numbers:
    print(num)
