import nltk, re, pprint
import feedparser
import unicodedata
from random import randint
from nltk import word_tokenize
from nltk.corpus import treebank, gutenberg, nps_chat
from urllib import request
from bs4 import BeautifulSoup
# satyri = "https://www.gutenberg.org/files/5225/5225-0.txt"
cnp = "https://www.gutenberg.org/files/2554/2554-0.txt"
# dorgray = "http://www.gutenberg.org/cache/epub/26740/pg26740.txt"
# impofearn = "http://www.gutenberg.org/cache/epub/844/pg844.txt"
# huckfinn = "https://www.gutenberg.org/files/76/76-0.txt"
# twocities = "https://www.gutenberg.org/files/98/98-0.txt"

url = cnp
response = request.urlopen(url)
raw = response.read().decode('utf8')

# start = raw.find("PART I")
# end = raw.rfind("End of Project Gutenberg's Crime")
# raw = raw[start:end]
# tokens = word_tokenize(raw)
# text = nltk.Text(tokens)
# sents = nltk.sent_tokenize(raw)
# pprint.pprint(sents[:30])
# llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
# print(llog['feed']['title'])
# for post in llog.entries:
    # print(post.title)
# print(llog.entries[1].title)
# content = llog.entries[1].content[0].value
# print(content[:80])
# raw = BeautifulSoup(content, 'html.parser').get_text()
# print(raw)
# tokes = word_tokenize(raw)
# print(tokes)
# a = [1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 2, 1]
# b = [' ' * 2 * (7 - i) + 'very' * i for i in a]
# for line in b:
#     print(line)

# path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
# f = open(path, encoding='latin2')
# for line in f:
#     print(line.strip())
#     print(line.strip().encode('unicode_escape'))
# lines =  open(path, encoding='latin2').readlines()
# line = lines[2]
# print(line.encode('unicode_escape'))
# for c in line:
#     if ord(c) > 127:
#         print('{} U+{:04x} {}'.format(c, ord(c), unicodedata.name(c)))

# m = re.search('\u015b\w*', line)
# print(m.group())

wlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

# textonyms = [w for w in wlist if re.search('^[ghi][mno][jlk][def]$', w)]

chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))

wsj = sorted(set(treebank.words()))

# fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))

# print([int(n) for n in re.findall(r'[0-9]{2,4}', '2009-12-31')])

regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
def compress(word):
    pieces = re.findall(regexp, word)
    return ''.join(pieces)

def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
# print("moby dick")
# print(moby.findall(r"<a> (<.*>) <man>"))
chat = nltk.Text(nps_chat.words())
# print("chat")
# print(chat.findall(r"<.*> (<.*>) <man>"))

# print(chat.findall(r"<a> (<.*>) <bro>"))
raw = """This will be a story of terror. It will be a story of police, a tale of darkness 
and of terror. But it will not seem so. It will not seem so because I am the one who tells it. 
I am the one who tells it and for that it will not seem so. But at its heart, this is the 
story of an appalling crime.
"""
"""
I am the friend of all Mexicans. I would say: I am the mother of Mexican poetry, 
but it is better that I don’t say it. I know all of the poets, and all of the poets know me. 
So, I would say that. I would say: I am the mother and a mother of a zephyr has blown for 
centuries, but I better not say it. I would say for example: I knew Arturito Belano when 
he was 16 and was a timid boy who wrote plays and poetry and didn’t know how to drink, 
but it would be to some extent a redundancy, and they taught me (with a lash they taught me, 
with a rod of iron) that the redundancies patronize and that the plot should suffice."""
tokens = word_tokenize(raw)
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
wnl = nltk.WordNetLemmatizer()
# print([porter.stem(t) for t in tokens])
# Porter is good for indexing texts for search
# Lancaster does

# print([lancaster.stem(t) for t in tokens])
# print([wnl.lemmatize(t) for t in tokens])

class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/4)                # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
            print(ldisplay, rdisplay)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()

# raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
#         though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
#         well without--Maybe it's always pepper that makes people hot-tempered,'..."""

	

def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words

def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = sum(len(word) + 1 for word in set(words))
    return text_size + lexicon_size

def flip(segs, pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs, randint(0, len(segs)-1))
    return segs

def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, round(temperature))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text, segs), segment(text, segs))
    print()
    return segs

# text1 = "whothefuckdoyouthinkiamtotalktomethatwayyoufoulsmellingmongoloidraccoon" 
# seg1 = "00100000000000000000000001000000000000000010000000000000000000000000000"
# anneal(text1, seg1, 5000, 1.2)

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
anneal(text, seg1, 5000, 1.2)
anneal(text, seg1, 500, 1.2)

raw = """Alas, poor Yorick! I knew him, Horatio: a fellow
of infinite jest, of most excellent fancy: he hath
borne me on his back a thousand times; and now, how
abhorred in my imagination it is! my gorge rims at
it. Here hung those lips that I have kissed I know
not how oft. Where be your gibes now? your
gambols? your songs? your flashes of merriment,
that were wont to set the table on a roar? Not one
now, to mock your own grinning? quite chap-fallen?
Now get you to my lady's chamber, and tell her, let
her paint an inch thick, to this favour she must
come; make her laugh at that. """
""