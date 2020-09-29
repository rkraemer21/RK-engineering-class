# defines two lists, one for each part of the equation
numbersSqrd = []
sqrNumbers = []

# easily changeable prompts
d = int(input("Starting number? > "))
f = int(input("Last number? > "))

# f + 1 so it's more intuitive for user (range doesn't include last number)
# makes numbersSqrd into a list of numbers x^2...y^2
for x in range(d, f + 1):
    numbersSqrd.append(x ** 2)

# makes a list of numbers x - y
for x in range(d, f + 1):
    sqrNumbers.append(x)

# squares the sum of numbers x - y, and removes the sum of x^2... y^2  -  then prints it
print(sum(sqrNumbers) ** 2 -sum(numbersSqrd))
