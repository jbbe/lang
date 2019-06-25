import nltk
from nltk.corpus import udhr

def find_language(word):
    opts = []
    for fileid in udhr.fileids():
        if word in udhr.words(fileid):
            opts.append(fileid)
    return opts

print(find_language('dom'))