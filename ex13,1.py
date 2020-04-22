from sys import argv

script, first, second = argv

print(script,"– The Calculator")
print(int(first)*int(input("What would you like to multiply the first variable by? ")))
print(int(second)/int(input("And what would you like to divide the second by? ")))
