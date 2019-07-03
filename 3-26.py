import nltk, re
from nltk.corpus import udhr, PlaintextCorpusReader

hung = udhr.raw('Spanish-Latin1')

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
hung = big_spanish_text
pattern  = r'(?x)[aeiou]{2}'
# vowel_seqs = nltk.regexp_tokenize(hung, pattern)
vowel_seqs = re.findall(pattern, hung)
seq_lists = [(seq[0], seq[1]) for seq in vowel_seqs]
print(seq_lists)
bigrams = nltk.bigrams(seq_lists)
print(bigrams)
fdist = nltk.FreqDist(seq_lists)
print(fdist.most_common(n=50))
# fdist.tabulate()
fdist.plot()