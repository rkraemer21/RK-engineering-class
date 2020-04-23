# question 41

#123456789

numbers = []

for x in range(123456789, 987654321): 
    for y in range(2, x // 2):
        if (x % y) == 0:
            numbers.append(x)

print(numbers)
