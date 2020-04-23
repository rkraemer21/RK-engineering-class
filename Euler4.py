# question 41

#123456789

numbers = []

for x in range(123456789, 987654321): 
    for y in range(2, x // 2):
        #if '1' in x and '2' in x and '3' in x and '4' in x and '5' in x and '6' in x and '7' in x and '8' in x and '9' in x and 
        if (x % y) == 0:
            numbers.append(x)

print(numbers)
