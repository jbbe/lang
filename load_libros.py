import nltk
from nltk.corpus import  PlaintextCorpusReader, swadesh, toolbox

def print_stats(corp):
    # Print avg word len, avg sent len, avg repeats per word
    print("w", "sent","repeats", "Title")
    for fileid in corp.fileids():
        num_chars = len(corp.raw(fileid))
        num_words = len(corp.words(fileid))
        num_sents = len(corp.sents(fileid))
        num_vocab = len(set(w.lower() for w in corp.words(fileid)))
        print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)   
# emma = nltk.Text(gutenberg.words('austen-emma.txt'))
# print(emma.concordance("bad"))
# corpus_root = '/usr/share/dict'
# wordlists = PlaintextCorpusReader(corpus_root, '.*')
corpus_root = '/Users/jbbe/interesa/txt_books'
file_names = ['amuleto.txt', 'putas_asesinas.txt', 'la_invencion_de_morel.txt', 'don_quixote.txt']
books = PlaintextCorpusReader(corpus_root, file_names)
# print(len(books.sents('amuleto.txt')))

# print(len(books.sents('putas_asesinas.txt')))
# print_stats(books)
# cfd = nltk.ConditionalFreqDist(
# 	(target, fileid[:4])
# 	for fileid in books.fileids()
# 	for w in books.words(fileid)
# 	for target in ['amor', 'desde']
# 	if w.lower().startswith(target))
# cfd.tabulate()
# cfd.plot()

# print(udhr.fileids())
# cfd = nltk.ConditionalFreqDist(
#                    (title, len(word))
#                    for title in file_names
#                    for word in books.words(title))
# cfd.plot(cumulative=False)
def lexical_diversity(my_text_data):
     word_count = len(my_text_data)
     vocab_size = len(set(my_text_data))
     diversity_score = vocab_size / word_count
     return diversity_score

def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word, end=' ')

        word = cfdist[word].max()

# text = books.words('don_quixote.txt')
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)
def stress(pron):
        return [char for phone in pron for char in phone if char.isdigit()]



# entries = nltk.corpus.cmudict.entries()
# print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'])

# Print out phonetics
# prondict = nltk.corpus.cmudict.dict()
# [ph for w in text for ph in prondict[w][0]]

# es2en = swadesh.entries(['es', 'en'])
# translate = dict(es2en)
# def average_sentence_length(text):
#     words = len(text.words())
#     sents = len(text.sents())
#     if words == 0:
#         return 0
#     return sents / words


# def modal_freqs(text):
#     fdist = nltk.FreqDist(w.lower() for w in news_text)
#     modals = ['can', 'could', 'may', 'might', 'must', 'will']
#     for m in modals:
#         print(m + ':', fdist[m], end=' ')
# # raw_text = udhr.raw('Spanish-Latin1')
# nltk.FreqDist(raw_text).plot(cumulative=True)



# languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']

# print(udhr.fileids())
# cfd = nltk.ConditionalFreqDist(
#                    (lang, len(word))
#                    for lang in languages
#                    for word in udhr.words(lang + '-Latin1'))
# cfd.plot(cumulative=False)









# from nltk.tokenize import word_tokenize
# sent = "the the the dog dog some other words that we do not care about"
# cfdist = nltk.ConditionalFreqDist()
# for word in word_tokenize(sent):
#     condition = len(word)
#     cfdist[condition][word] += 1
# print(cfdist, cfdist.conditions())
# cfdist.plot()

# nltk.download('inaugural')
# cfd = nltk.ConditionalFreqDist(
# 	(target, fileid[:4])
# 	for fileid in inaugural.fileids()
# 	for w in inaugural.words(fileid)
# 	for target in ['change', 'status quo']
# 	if w.lower().startswith(target))
# cfd.tabulate()
# cfd.plot()

from nltk.corpus import wordnet as wn
motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
types_of_motorcar[0]
print(sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()))

print(motorcar.hypernyms())
paths = 