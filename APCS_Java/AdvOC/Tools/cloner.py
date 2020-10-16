from sys import argv
from os.path import exists

script, ffile, tfile = argv

indata = open(ffile).read()

print(f"The input file is {len(indata)} bytes long.")
print(f"Does the output file exist? {exists(tfile)}")

out_file = open(tfile, 'w')
out_file.write(indata)

out_file.close()

