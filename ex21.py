def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(10, 7)
height = subtract(62, 4)
weight = multiply(65, 2)
iq = divide(100, 2)

print(f"{age}, {height}, {weight}, {iq}")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#different ways of printing the same thing
# 17 + (58 - (130 * (50 / 2)))
print(what)
print(add(17, subtract(58, multiply(130, divide(50, 2)))))

# 24 + 34 / 100 - 1023
what2 = add(subtract(24, 1023), divide(34, 100))
print(what2)

# 86 / 34 + 67 * 21 / 3 + 7
what3 = add(add(divide(86, 34), divide(multiply(67, 21), 3)), 7)
print(what3)

# 98 / (84 + 53) - 45 * 8 + 67 * 9
what4 = add(subtract(divide(98, add(84, 53)), multiply(45, 8)), multiply(67, 9))
print(what4)
