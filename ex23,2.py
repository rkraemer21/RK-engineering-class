import sys

script, iencoding, error = sys.argv


def main(lfile, encoding, errors):
    line = lfile.readline()

    if line:
        printline(line, encoding, errors)
        return main(lfile, encoding, errors)


def printline(line, encoding, errors):
    nlang = line.strip()
    rawbytes = nlang.encode(encoding, errors=errors)
    #cookstring = rawbytes.decode(encoding, errors=errors)
    #rbytes = bytes(nlang, encoding=encoding, errors=errors)    

    langencoded.write(rawbytes)
    #langencoded.write(rbytes)

languages = open("languages.txt", encoding="utf-8")
#langencoded.txt is a blank file that I want to write the encoded characters to
langencoded = open('langencoded.txt', 'a')

main(languages, iencoding, error)
