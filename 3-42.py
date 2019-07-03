import nltk
from nltk.corpus import wordnet as wn
 	

class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))
        self._wnindex = nltk.Index((self._wnoffset(word), i)
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
        for i in self._wnindex[key]:
            if i not in self._index[key]:
                lcontext = ' '.join(self._text[i-wc:i])
                rcontext = ' '.join(self._text[i:i+wc])
                ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
                rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
                print(ldisplay, rdisplay)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()

    def _wnoffset(self, word):
        if len(wn.synsets(word.lower())) == 0:
            return
        return wn.synsets(word.lower())[0].offset

# hamlet = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')
porter = nltk.PorterStemmer()
# lancaster = nltk.LancasterStemmer()
# hamport = IndexedText(nltk.PorterStemmer(), hamlet)
# hamlan = IndexedText(lancaster, hamlet)
# print(hamdex.concordance('horatio'))
text = IndexedText(porter, nltk.corpus.webtext.words('grail.txt'))
print(text.concordance('lie'))
