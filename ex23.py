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
    cookstring = rawbytes.decode(encoding, errors=errors)

    print(rawbytes,"<===>", cookstring, nlang)

languages = open("languages.txt", encoding="utf-8")

main(languages, iencoding, error)
