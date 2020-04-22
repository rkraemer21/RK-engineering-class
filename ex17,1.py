from sys import argv ; from os.path import exists ; script, ffile, tfile = argv ; indata = open(ffile).read() ; outfile = open(tfile, 'w') ; outfile.write(indata) ; outfile.close()
#out_file = open(tfile, 'w')
#out_file.write(indata)
#out_file.close()
