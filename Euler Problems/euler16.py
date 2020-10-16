# just for more freedom.  The question asks for 2^1000.  You do have to be careful how big your power is.
d = int(input("Base number? > "))
f = int(input("Exponent? > "))

#makes it a string so you can go digit by digit
v = str(d ** f)

numbers = []

# add every digit separately to a list
for x in v:
    x = int(x)
    numbers.append(x)

# add all the digits together and print
print(sum(numbers))
