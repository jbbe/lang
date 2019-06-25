
import nltk
from nltk.corpus import  PlaintextCorpusReader, brown, stopwords
from random import choice, randint
from string import ascii_uppercase, ascii_lowercase, digits


corpus_root = '/Users/jbbe/interesa/txt_books'
file_names = ['amuleto.txt', 'estrella_distante.txt', 'putas_asesinas.txt', 'det_salv_bol.txt', 
                'la_invencion_de_morel.txt', 'don_quixote.txt', 
                'borges_ficc.txt', 'hot_sur.txt', 'diez_muj.txt', 'rayuela-cortazar.txt']
books = PlaintextCorpusReader(corpus_root, file_names)

big_spanish_text = books.words('det_salv_bol.txt') + books.words('don_quixote.txt') + books.words('rayuela-cortazar.txt')


punctuation = [',', '.', '?', '\'', '!', '¿', '(', ')', ':', ';', '-', 
                '«', '...', '».', '—.', '—,', '?,', '!),', '—']
def bigram_no_contains_stop(bigram):
        # if bigram[0] in stopwords.words(lang):
        #         return False
        # if bigram[1] in stopwords.words(lang):
        #         return False
        if bigram[0] in punctuation: 
                return False
        if bigram[1] in punctuation:
                return False
        return True

def stripped_bigrams(text):
        bigrams = nltk.bigrams(text)
        bigrams_no_stops = [bigram for bigram in bigrams if bigram_no_contains_stop(bigram)]
        return bigrams_no_stops
        # fdist = nltk.FreqDist(bigrams_no_stops)
        # # cfd.tabulate()
        # return fdist

def generate_model(cfdist, word, num=15, n=5):
    for i in range(num):
        if word is None:
                return
        print(word, end=' ')
        if len(cfdist[word]) == 0:
                return
        if len(cfdist[word]) < n:
                word = choice(cfdist[word].most_common(n=len(cfdist[word]))) 
        else:
                word = choice(cfdist[word].most_common(n=n))[0]


def gen_sentence_for_brown_cats(starter_word, length):
    word = starter_word.lower()
    for cat in brown.categories():
        # cfd = nltk.ConditionalFreqDist(stripped_bigrams(nltk.bigrams(brown.words(categories=cat))))
        cfd = nltk.ConditionalFreqDist(nltk.bigrams(brown.words(categories=cat)))
        print(cat, ':')
        (generate_model(cfd, word, length))
        print('\n')

gen_sentence_for_brown_cats("love", 20)


cfd = nltk.ConditionalFreqDist(nltk.bigrams(brown.words(categories=brown.categories())))
generate_model(cfd, "Such", 20)