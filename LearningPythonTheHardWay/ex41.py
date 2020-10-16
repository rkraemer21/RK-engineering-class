import random
from urllib.request import urlopen
import sys

WORD_URL = 'http://learncodethehardway.org/words.txt'
words = []

phrases = {
    'class %%%(%%%):':
      'Make a class named %%% that is-a %%%.',
    'class %%%(object):\n\tdef __init_(self, ***)':
      'clas %%% has-a __init__ that takes self and *** parameters.',
    'class %%%(object):\n\tdef ***(self, @@@)':
      'class %%% has-a function *** that takes self and *** parameters.',
    '*** = %%%()':
      'Set *** to an instance of class %%%.',
    '***.***(@@@)':
      'From *** get the *** function, call it with self and @@@ parameters.',
    '***.*** = "***"':
      'From *** get the *** attribute and set it to "***".'
}


if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False


for word in urlopen(WORD_URL).readlines():
    words.append(str(word.strip(), encoding = 'utf-8'))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(words, snippet.count('%%%'))]

    other_names = random.sample(words, snippet.count('***'))
    results = []
    paramNames = []

    for i in range(0, snippet.count('@@@')):
        paramCount = random.randint(1,3)
        paramNames.append(', '.join(random.sample(words, paramCount)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace('%%%', word, 1)

        for word in other_names:
            result = result.replace('***', word, 1)

        for word in paramNames:
            result = result.replace('@@@', word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = list(phrases.keys())
        random.shuffle(snippets)
 
        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input('> ')
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print('Bye.')
