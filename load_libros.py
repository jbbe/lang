import nltk
from nltk.corpus import  PlaintextCorpusReader, swadesh, toolbox, brown

def lexical_diversity(my_text_data):
     word_count = len(my_text_data)
     vocab_size = len(set(my_text_data))
     diversity_score = vocab_size / word_count
     return diversity_score


def print_stats(corp):
    # Print avg word len, avg sent len, avg repeats per word
    print("w", "sent","reps", "div", "Title")
    for fileid in corp.fileids():
        num_chars = len(corp.raw(fileid))
        num_words = len(corp.words(fileid))
        num_sents = len(corp.sents(fileid))
        num_vocab = len(set(w.lower() for w in corp.words(fileid)))
        print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), lexical_diversity(corp.words(fileid)), fileid)   
# emma = nltk.Text(gutenberg.words('austen-emma.txt'))
# print(emma.concordance("bad"))
# corpus_root = '/usr/share/dict'
# wordlists = PlaintextCorpusReader(corpus_root, '.*')
corpus_root = '/Users/jbbe/interesa/txt_books'
file_names = ['amuleto.txt', 'estrella_distante.txt', 'putas_asesinas.txt', 'det_salv_bol.txt', 
                'la_invencion_de_morel.txt', 'don_quixote.txt', 
                'borges_ficc.txt', 'hot_sur.txt', 'diez_muj.txt', 'rayuela-cortazar.txt']
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
import random

def generate_model(cfdist, word, num=15, n=5):
    for i in range(num):
        if word is None:
                return
        print(word, end=' ')
        if len(cfdist[word]) == 0:
                return
        if len(cfdist[word]) < n:
                word = random.choice(cfdist[word].most_common(n=len(cfdist[word]))) 
        else:
                word = random.choice(cfdist[word].most_common(n=n))[0]


big_spanish_text = books.words('det_salv_bol.txt') + books.words('don_quixote.txt') + books.words('rayuela-cortazar.txt')
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)
# generate_model(cfd, 'mujer', num=20, n=7)

# text = books.words('don_quixote.txt')
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)
# print(generate_model(cfd, 'mujer', num=20, n=10))
# text = books.words('rayuela-cortazar.txt')
# bigrams = nltk.bigrams(text)
# cfd = nltk.ConditionalFreqDist(bigrams)
# print(generate_model(cfd, 'mujer', num=20, n=10))
def stress(pron):
        return [char for phone in pron for char in phone if char.isdigit()]

modals = ['can', 'could', 'may', 'might', 'must', 'will']

def type_occurance(targets, cats=brown.categories()):
        cfd = nltk.ConditionalFreqDist(
                (genre, word)
                for genre in cats
                for word in brown.words(categories=genre))
        cfd.tabulate(conditions=cats, samples=targets)
        # for word in targets:
        #         print(word, sep=' ')
        # print('\n')
        # for cat in cats:
        #         fdist = nltk.FreqDist(w.lower() for w in brown.words(categories=cat))
        #         for word in targets:
        #                 print(fdist[word], sep=' ')

# type_occurance(modals)
gud = ["good", "evil", "bad", "divine", "vile"]
profanity = ["fuck", "bitch", "shit", "pussy", "cock", "ass", "damn"]
# type_occurance(gud)
# type_occurance(profanity)
# entries = nltk.corpus.cmudict.entries()
# print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'])

# Print out phonetics
prondict = nltk.corpus.cmudict.dict()
# print(len(prondict))
# [ph for w in text for ph in prondict[w][0]]
# print(len([w for w in prondict if len(prondict[w]) > 1]))
# print(len([w for w in prondict if len(prondict[w]) > 1])/len(prondict))
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
# motorcar = wn.synset('car.n.01')
# types_of_motorcar = motorcar.hyponyms()
# types_of_motorcar[0]
# print(sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas()))

# print(motorcar.hypernyms())
# paths = motorcar.hypernym_paths()
# for synset in wn.synsets('mint', wn.NOUN):
#         print(synset.name() + ':', synset.definition())

def wordnet_list(word):
        for synset in wn.synsets(word):
                print(synset,
                        'member mero',
                        synset.member_meronyms(),
                        'part mero',
                        synset.part_meronyms(),
                        'substance mero',
                        synset.substance_meronyms(),
                        'member holo',
                        synset.member_holonyms(),
                        'part holo',
                        synset.part_holonyms(),
                        'substance holo',
                        synset.substance_holonyms()
                        )
                



# from nltk.corpus import verbnet as vn
# print(len([noun for noun in wn.all_synsets('n') if noun.hyponyms() == []]))
# union = nltk.corpus.state_union
# for speech in union.fileids():
#         men = union.raw(speech).count('men')
#         women = union.raw(speech).count('women')
#         people = union.raw(speech).count('people')
#         print(speech, men, women, people)

# cfd = nltk.ConditionalFreqDist(
#                  	(target, fileid[:4])
# 	                for fileid in union.fileids()
# 	                for w in union.words(fileid)
# 	                for target in ['men', 'women', 'people']
# 	                if w.lower().startswith(target))

# cfd.plot()

# from nltk.corpus import brown
# for cat in brown.categories():
#         for sent in brown.sents(categories=cat):
#                 if sent[0] == "Further":
#                         print(cat, ' '.join(sent[0:12]))
def find_usage_across_brown(word):
        for cat in brown.categories():
                for sent in brown.sents(categories=cat):
                        if sent[0] == word:
                                print(cat, ' '.join(sent[0:12])) 
# for cat in brown.categories():
#         print(nltk.Text(brown.words(categories=cat)).concordance("However"))


# from nltk.corpus import names


# cfd = nltk.ConditionalFreqDist(
#                         (fileid, name[0])
#                         for fileid in names.fileids()
#                         for name in names.words(fileid))

# cfd.plot()

def concordance_across_texts(corp, word):
    for fileid in corp.fileids():
        print(fileid, ":")
        print(nltk.Text(corp.words(fileid)).concordance(word))

# concordance_across_texts(books, 'paz')
# concordance_across_texts(books, 'capaz')

def supergloss(s):
       defs = ''
       defs = defs+ (s.definition())
       for hyper in s.hypernyms():
               defs = defs + (hyper.definition())
       for hypo in s.hyponyms():
                defs = defs + (hypo.definition())
       return defs

# print(supergloss(wn.synset('food.n.01')))

def three_in_brown():
        # wordset = set(brown.words(categories=brown.categories()))
        wordset = set(brown.words(categories='humor'))
        # return [word for word in wordset if brown.words(categories=brown.categories()).count(word) > 2]
        return [word for word in wordset if brown.words(categories='humor').count(word) > 2]

def word_frequency_in_brown(word, category):
        return brown.words(categories=category).count(word) /len(brown.words(categories=category))

# print(word_frequency_in_brown('bad', 'news'))
# print(three_in_brown())
def Sort_Tuple(tup):  
  
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    return(sorted(tup, key = lambda x: x[1]))   
  

from nltk.corpus import stopwords
# for cat in brown.categories():
#         print(cat, ' '* (15-len(cat)), lexical_diversity(brown.words(categories=cat)))


# def most_common_non_stop_words(text):
#         words = []
#         for word in set(text):
#                 if word not in stopwords.words('english'):
#                         words.append(tuple([word, text.count(word)]))
#                         print(word)
#         ret = Sort_Tuple(words)[:50]
#         return ret

# print(most_common_non_stop_words(brown.words(categories='news')))
# most_common_bigrams(brown.words(categories='humor'))

punctuation = [',', '.', '?', '\'', '!', '¿', '(', ')', ':', ';', '-', 
                '«', '...', '».', '—.', '—,', '?,', '!),', '—']
# print(stopwords.words('spanish'))
def most_common_non_stop_words(text):
    fdist = nltk.FreqDist([w.lower() for w in text if w.lower() not in stopwords.words('spanish') and w.lower() not in punctuation])
    return fdist.most_common(n=50)

# for fid in books.fileids():
#         most_common_non_stop_words(books.words(fid)).tabulate()
#         print(fid, most_common_non_stop_words(books.words(fid)))

def bigram_no_contains_stop(bigram, lang):
        if bigram[0] in stopwords.words(lang):
                return False
        if bigram[1] in stopwords.words(lang):
                return False
        if bigram[0] in punctuation: 
                return False
        if bigram[1] in punctuation:
                return False
        return True

def most_common_bigrams(text, lang):
        bigrams = nltk.bigrams(text)
        bigrams_no_stops = [bigram for bigram in bigrams if bigram_no_contains_stop(bigram, lang)]
        fdist = nltk.FreqDist(bigrams_no_stops)
        # cfd.tabulate()
        return fdist.most_common(n=50)

# for fid in books.fileids():
#         # most_common_bigrams(books.words(fid)).tabulate()
#         print(fid, most_common_bigrams(books.words(fid), 'spanish'))

# print(most_common_bigrams(brown.words(categories='news'), 'english'))

# bigrams = nltk.bigrams(brown.words(categories='humor'))
# print(bigrams)
# bigrams_no_stops = [bigram for bigram in bigrams if bigram_no_contains_stop(bigram, 'english')]
# print(bigrams_no_stops)
# fdist = nltk.FreqDist(bigrams_no_stops)
# print(fdist.most_common(n=50))

def compute_syllables(text):
    syllables = 0
    for word in text:
            if word in prondict:
                    syllables = syllables + len(prondict[word])
            else:
                syllables = syllables + 1

    return syllables



def hedge(text):
        i = 0
        for i in range(len(text)):
                if i % 3 == 0 and i != 0:
                        text.insert(i, 'like')
        return text

# bad_text = ['ok', 'what', 'the', 'fook', 'are', 'you', 'thinking', 'i', 'dont', 'know', 'what', 'to', 'say']
# print(hedge(bad_text))
import numpy
import matplotlib.pyplot as plt
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
        txt = ''
        for i in range(length):
                random.choice("")