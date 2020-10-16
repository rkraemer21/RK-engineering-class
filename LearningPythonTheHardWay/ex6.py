 typo_ppl
typo_ppl = 10
#define x, which is set up to be an f-string with typo_ppl inside
x = f"There are {typo_ppl} types of people."

#define binary, which is a string with quotes so that it doesn't think the left side is a variable - it's a string, just that
binary = "binary"
#same thing as above (I wonder what happens if you have two conjunctions in a string
dont = "don't"

#define those two into a sentence in an f-string so it can print all as one with an easy 'print(y)'
y = f"Those who know {binary} and those who {dont}."

#print all of x, and because the (x) is in parentheses, it all works
print(x)
#print all of y, same as above
print(y)

# this creates an f-string inside of an f-string, which makes me curious
print(f"I said: {x}")
#same thing as above but with quotes around y, interesting
print(f"I also said: '{y}'")

#defines the variable 'hilarious' as the string 'false'
hilarious = 'false'

#defines the variable (note = sign) jokeval as a string with {} in it, setting it up for the new format thingy
jokeval = "Is'nt that joke so funny?! {}"

#new syntax, i dont fully understand it. maybe it formats 'hilarious' into each of the {} in jokeval
print(jokeval.format(hilarious))

#defines w as a string
w = "This is the left side of..."
#defines e as a string
e = "a string with a right side."

#prints w and e together, in that order
print(w+e + binary)
