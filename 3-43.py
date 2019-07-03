import nltk
from nltk.corpus import udhr, swadesh
from collections import Counter
from statistics import mode

# go through text and make list of possible langs for each word 
# and return the most frequent across these lists

def find_language_word(word):
    opts = []
    # print(word)
    for fileid in udhr.fileids():
        if word in udhr.words(fileid)[:len(udhr.words(fileid)/4)]:
            opts.append(fileid)
    return opts

def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm) 

def find_language_text(text):
    possibilities = []
    for word in set(text):
        langs = find_language_word(word)
        if len(langs) > 0:
            # print(langs)
            for lang in langs:
                possibilities.append(lang)
    # print(possibilities)
    # tops = []
    # counter_obj = Counter(possibilities)
    # return counter_obj.most_common(1)[0][0]
    # print(possibilities)
    return most_frequent(possibilities)

languages = ['English', 'German_Deutsch',
            'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik', 'Spanish']

for language in languages:
    print(language, find_language_text(udhr.words(language+'-Latin1')))