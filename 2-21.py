import nltk
from nltk.corpus import brown
prondict = nltk.corpus.cmudict.dict()

# syllable counts by genre
def compute_syllables(text):
    syllables = 0
    for word in text:
            if word in prondict:
                    syllables = syllables + len(prondict[word])
            else:
                syllables = syllables + 1

    return syllables

news_syl = compute_syllables(brown.words(categories='news'))

humor_syl = compute_syllables(brown.words(categories='humor'))

for cat in brown.categories():
    syl_count = compute_syllables(brown.words(categories=cat))
    print(cat, ' '*(15-len(cat)), syl_count, ' '*(10-len(str(syl_count))), syl_count/len(brown.words(categories=cat)))