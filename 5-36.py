import nltk, re
from nltk.corpus import brown


patterns = [
    (r'^(or|and|both|but|either|for|neither|Or|And)$', 'CC'),          # Determiners
    (r'^(the|a|an|some|most|every|which|The|A|An|Some)$', 'AT'),          # Determiners
    (r'^([Hh]e|[Ss]he|[Tt]hey)$', 'PPS'),          # Determiners
    (r'.*ing$', 'VBG'),               # gerunds
    # (r'.*eed', 'VBN'),
    (r'.*ed$', 'VBD'),                # simple past
    (r'.*es$', 'VBZ'),                # 3rd singular present
    (r'.*pone$', 'VBP'),                # 3rd singular present
    (r'.*ould$', 'MD'),               # modals
    (r'[Ww]ill', 'MD'),               # modals
    (r'[Bb]e', 'BE'),               # modals

    (r'.*\'s$', 'NN$'),               # possessive nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
    # (r'.*est$', 'RBS'),                  #Adverb
    (r'.*ier$', 'RBR'),                  #Adverb
    (r'.*ly$', 'RB'),                  #Adverb
    (r'[wW]h.*', 'WDT'),
    (r'[Ii]t', 'PPS'),
    (r'[Hh]as', 'HVZ'),
    (r'^(her|his|mine|my|our|ours|their|thy|your|Her|His)$', 'PRP$'),
    (r'.*self$', 'PRP'),
    (r'.*able$', 'JJ'),                  #Adverb
    (r'.*ive$', 'JJ'),                  #Adverb
    (r',', ','),        # Comma
    (r'\(', '('),        # Comma
    (r'\)', ')'),        # Comma
    (r'[\.!\?]', '.'),        # Comma
    (r'"', '"'),
    (r'[\:;]', ':'),        # Comma,
    (r'``', '``'),
    (r'\'\'', '\'\''),
    (r'^([Oo]f|[Bb]y|[iI]n)$', 'IN'),
    (r'.*ever.*', 'WRB'),
    (r'.*ous$', 'JJ'),                     # nouns (default)
    (r'(are|is)', 'BER'),
    (r'.*quate$', 'JJ'),                     # nouns (default)
    (r'.*s$', 'NNS'),                 # plural nouns
    (r'.*id', 'VBD'),
    (r'.*uce', 'VB'),
    (r'been', 'BEN'),
    (r'upon', 'RB'),
    (r'[tT]o', 'TO'),

    # (r'[A-Z].*', 'NNP')
    (r'.*', 'NN')                     # nouns (default)
]
brown_tagged_sents = brown.tagged_sents(categories=['news','fiction'])
regexp_tagger = nltk.RegexpTagger(patterns)
brown_sents = brown.sents(categories='news')
# print(regexp_tagger.tag(brown_sents[75]), '\n', brown_tagged_sents[75])
# print(regexp_tagger.evaluate(brown_tagged_sents))

  	

def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))


size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
t_reg = nltk.RegexpTagger(patterns)
t1 = nltk.UnigramTagger(train_sents, backoff=t_reg)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)
print(t_reg.evaluate(test_sents))
print(t1.evaluate(test_sents))
print(t2.evaluate(test_sents))
print(t3.evaluate(test_sents))

from pickle import dump
output = open('t3.pkl', 'wb')
dump(t3, output, -1)
output.close()


from pickle import load
input = open('t3.pkl', 'rb')
tagger = load(input)
input.close()