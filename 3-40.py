import nltk
from nltk.corpus import abc, PlaintextCorpusReader, udhr

def ari(fileid):
    """Accept text as list of words"""
    print(fileid)
    num_chars = len(abc.raw(fileid))
    num_words = len(abc.words(fileid))
    num_sents = len(abc.sents(fileid))

    avg_word_len = num_chars / num_words
    avg_sent_len = num_words / num_sents

    return avg_word_len * 4.71 + avg_sent_len * 0.5 - 21.43

# aris = [(f, ari(f)) for f in abc.fileids()]
# print(aris)

alas = """Alas, poor Yorick! I knew him, Horatio: a fellow
of infinite jest, of most excellent fancy: he hath
borne me on his back a thousand times; and now, how
abhorred in my imagination it is! my gorge rims at
it. Here hung those lips that I have kissed I know
not how oft. Where be your gibes now? your
gambols? your songs? your flashes of merr-\niment,
that were wont to set the table on a roar? Not one
now, to mock your own grinning? quite chap-fallen?
Now get you to my lady's cha-\nmber, and tell her, let
her paint an inch thick, to this favour she must
come; make her laugh at that. """
# sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
# print('\n-----\n'.join(sent_detector.tokenize(alas.strip())))


def raw_ari(raw):
    """Accept text as list of words"""
    num_chars = len(raw)
    num_words = len(nltk.word_tokenize(raw))
    sent_detector = nltk.data.load('tokenizers/punkt/spanish.pickle')
    num_sents = len(sent_detector.tokenize(alas.strip()))

    avg_word_len = num_chars / num_words
    avg_sent_len = num_words / num_sents
    print(avg_word_len, avg_sent_len)
    return (avg_word_len * 4.71) + (avg_sent_len * 0.5) - 21.43
# print(ari(alas))
corpus_root = '/Users/jbbe/interesa/txt_books'
file_names = ['amuleto.txt', 'estrella_distante.txt', 'putas_asesinas.txt', 'det_salv_bol.txt', 'sav_det.txt',
                'la_invencion_de_morel.txt', 'don_quixote.txt', 
                'borges_ficc.txt', 'hot_sur.txt', 'diez_muj.txt', 'rayuela-cortazar.txt']
vowels = ['a', 'e', 'i', 'o', 'u']

books = PlaintextCorpusReader(corpus_root, file_names)
big_spanish_text = ''.join([books.raw('det_salv_bol.txt'), 
                            books.raw('don_quixote.txt'), 
                            books.raw('rayuela-cortazar.txt'),
                            books.raw('borges_ficc.txt'),
                            books.raw('amuleto.txt'),
                            books.raw('estrella_distante.txt'),
                            books.raw('la_invencion_de_morel.txt'),
                            books.raw('hot_sur.txt')])


hung = udhr.raw('Spanish-Latin1')

print('udhr span', raw_ari(hung))
print('big span', raw_ari(big_spanish_text))