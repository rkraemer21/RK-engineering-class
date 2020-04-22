from sys import argv

def print2(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print22(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print1(arg1):
    print(f"arg1: {arg1}")

def print0():
    print("I got nothin'.")

def printme(arg1):
    print(f"Here's what you typed: {arg1}")

script, thing = argv

def printthat(arg1):
    print(f"You also input this: {thing}")

print2("Ryan", "Kraemer")
print22("Ryan", "Kraemer")
print1("First!")
print0()
printme(input())
printthat(thing)
