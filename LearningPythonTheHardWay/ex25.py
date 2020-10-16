def bwords(stuff):
    words = stuff.split(' ') 
    return words

def sowords(words):
    return sorted(words)

def pfword(words):
    word = words.pop()
    print(word)

def plword(words):
    word = words.pop(-1)
    print(word)

def ssentence(sentence):
    words = bwords(sentence)
    return sowords(words)

def pfal(sentence):
    words = bwords(sentence)
    pfword(words)
    plword(words)

def pfalsorted(sentence):
    words = ssentence(sentence)
    pfword(words)
    plword(words)
