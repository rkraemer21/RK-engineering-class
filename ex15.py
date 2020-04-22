#takes the module argv from system, allowing me to input the meat of the matter
from sys import argv

#defines the things in that order for me to input with argv
script, filename = argv

#defines txt as the file that i input
txt = open(filename)

#says a useless thing
print(f"""Here's your file {filename}.
""")
#reads and subsequently prints the file
print(txt.read())

txt.close()

#another way of me inputting the file name, but a separate way altogether, using input instead of argv
file2 = input("Print the file name again\n> ")

#defines txt2 as the file
txt2 = open(file2)

#reads and prints the file
print(txt2.read())
print(open(filename).read())

txt2.close()
