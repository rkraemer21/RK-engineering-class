from sys import argv

script, ifile = argv

cfile = open(ifile)

print(cfile.readline())

print(cfile.readline())

print(cfile.readline())

cfile.seek(0)

print(cfile.readline())

cfile.close()
