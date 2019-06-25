import nltk
from nltk.corpus import PlaintextCorpusReader
import numpy
import matplotlib.pyplot as plt
from random import choice, randint
from string import ascii_uppercase, ascii_lowercase, digits


corpus_root = '/Users/jbbe/interesa/txt_books'
file_names = ['amuleto.txt', 'estrella_distante.txt', 'putas_asesinas.txt', 'det_salv_bol.txt', 
                'la_invencion_de_morel.txt', 'don_quixote.txt', 
                'borges_ficc.txt', 'hot_sur.txt', 'diez_muj.txt', 'rayuela-cortazar.txt']
books = PlaintextCorpusReader(corpus_root, file_names)

big_spanish_text = books.words('det_salv_bol.txt') + books.words('don_quixote.txt') + books.words('rayuela-cortazar.txt')

def zipf(text):
        fdist = nltk.FreqDist(text)
        freqs = []
        for word in fdist:
                freqs.append(fdist[word])
        x_coordinate = [i for i in range(len(freqs)) ]
        plt.yscale('log')
        plt.plot(x_coordinate, sorted(freqs, reverse=True))
        plt.show()

zipf(big_spanish_text)

def gen_rnd_txt(length=100):
    dic = ascii_uppercase + ascii_lowercase
    txt = ''
    for i in range(length):
            new = ''.join(choice(dic) for i in range(randint(0,10)))
            txt = txt + ' ' + new
    return txt

zipf(gen_rnd_txt(20000))