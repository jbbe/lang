import nltk


from nltk.corpus import brown
# brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
# tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
# tag_fd.most_common()
# # tag_fd.plot(cumulative=True)
# nltk.app.concordance()
# word_tag_pairs = nltk.bigrams(brown_news_tagged)
# # noun_preceders = [b[1] for (a, b) in word_tag_pairs if a[1] == 'NOUN']
# # fdist = nltk.FreqDist(noun_preceders)
# # print([tag for (tag, _) in fdist.most_common()])
# wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
# verb_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'VERB']
# fdist = nltk.FreqDist(verb_preceders)
# # print(word_tag_pairs)
# # print([tag for (tag, _) in fdist.most_common()])
# word_tag_fd = nltk.FreqDist(wsj)
# # print([wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB'])
# cfd1 = nltk.ConditionalFreqDist(wsj)
# wsj = nltk.corpus.treebank.tagged_words()
# cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
# # print([w for w in cfd1.conditions() if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]])
# past_participles = list(cfd2['VBN'])
# word_tag_pairs = nltk.bigrams(brown_news_tagged)
# preceding_pp = [a[0] for (a, b) in word_tag_pairs if b[0] in past_participles]
# # print(cfd2['VBN'], past_participles, preceding_pp)
# fdist = nltk.FreqDist(preceding_pp)
# # print(fdist.most_common())

  	

# def findtags(tag_prefix, tagged_text):
#     cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
#                                   if tag.startswith(tag_prefix))
#     return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())

# tagdict = findtags('VB', nltk.corpus.brown.tagged_words(categories='news'))
# # for tag in sorted(tagdict):
#     # print(tag, tagdict[tag])

# # brown_learned_text = brown.words(categories='learned')
# # often_precedent = sorted(set(b for (a, b) in nltk.bigrams(brown_learned_text) if a == 'often'))
# # print(often_precedent)
# brown_lrnd_tagged = brown.tagged_words(categories='learned', tagset='universal')
# tags = [b[1] for (a, b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'frequently']
# fd = nltk.FreqDist(tags)
# # fd.tabulate()


from nltk.corpus import brown
# def process(sentence):
#     for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
#         if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
#             print(w1, w2, w3)
# for tagged_sent in brown.tagged_sents():
#     process(tagged_sent)


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
    # (r'(an|another|any|del|each|either|half|many|much|nary|neither|some|such|them)', 'DT'),
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

def display():
    import pylab
    word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
    words_by_freq = [w for (w, _) in word_freqs]
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()
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