print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n new lines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t where there is none.
"""

print('––––––––')
print(poem)
print('––––––––')


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secretform(started):
    jellybeans = started * 500
    jars = jellybeans / 1000
    crates = jars / 100
    return jellybeans, jars, crates


startpoint = 10000
beans, jars, crates = secretform(startpoint)


print("With a starting point of : {}".format(startpoint))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

startpoint /= 10

print("We can also do that this way:")
formula = secretform(startpoint)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
