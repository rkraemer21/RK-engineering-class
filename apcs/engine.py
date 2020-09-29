from sys import argv
script, runFile, arg2 = argv

arg2 = int(arg2)

for x in range(0, arg2):
    print(x)

print(runFile) 

os.system('python3 {runFile}')
