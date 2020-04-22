formatter = "{} {} {} {}"

print(formatter.format(2,1,4,3))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"And now I", 
	"will let her go", 
	"because she", 
	"will never, ever know"
	))

formatter = 1
print(formatter)

