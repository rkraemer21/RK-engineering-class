#takes the argv module from sys
from sys import argv

#defines script and ifile as the inputs for argv
script, ifile = argv

#defines printall as a function that reads and prints the opened file cfile, which is a version of the input file
def printall(f):
    print(f.read())

#defines reqind as a function that puts the reader back to line 0 on the file. seek is a function being run on f, which is the input
def rewind(f):
    f.seek(0)

#defines printline as printing a certain line from the file, i'm not exactly sure how this works with the print function
def printline(lc, f):
    print(lc, f.readline(), end = ' ')

#opens the file and redefines it
cfile = open(ifile)

#says something dumb
print("First let's print the whole file:\n")

#reads and then prints the cfile
printall(cfile)

#dumb
print("Now let's rewind, kind of like a tape:\n")

#puts the reader at line 0 on the file
rewind(cfile)

#dumb
print("Let's print three lines:\n")

#defines the line to be read as number 1, then inputs that line and specifies the file to read the line
cline = 1
printline(cline, cfile)

#plus one, same thing
cline += 1
printline(cline, cfile)

#plus one, same thing
cline +=1
printline(cline, cfile)
