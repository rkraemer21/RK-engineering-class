thecount = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for number in thecount:
    print(f"This is count {number}")


for fruit in fruits:
    print(f"A fruit of type: {fruit}")



for num in change:
    print(f"I got {num}")


elements = []


#for i in range(2, 6):
    #print(f"Adding {i} to the list.")
    #elements.append(i)

i = range(0,6)
elements.append(i)


for i in elements:
    print(f"Element was type {i}.")
