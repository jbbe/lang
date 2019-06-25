import nltk
from nltk.corpus import wordnet as wn
from collections import OrderedDict
pairs = {'car': 'automobile',
         'gem': 'jewel',
         'journey': 'car',
         'boy': 'lad',
         'coast': 'forest',
         'asylum': 'madhouse',
         'magician': 'wizard',
         'midday': 'noon',
         'furnace': 'stove',
         'food': 'rooster',
         'bird': 'crane', 
         'tool': 'implement',
         'brother': 'monk',
         'lad': 'wizard',
         'crane': 'implement',
         'monk': 'slave',
         'cemetery': 'woodland',
         'forest': 'graveyard', 
         'shore': 'woodland', 
         'chord': 'smile', 
         'glass': 'magician', 
         'rooster': 'voyage', 
         'noon': 'string'}

def similarity(a, b):
    a_sets = []
    b_sets = []
    shortest_path = None
    for synset in wn.synsets(a, wn.NOUN):
        a_sets.append(synset)
    
    for synset in wn.synsets(b, wn.NOUN):
        b_sets.append(synset)

    for synset in wn.synsets(a, wn.VERB):
        a_sets.append(synset)
    
    for synset in wn.synsets(b, wn.VERB):
        b_sets.append(synset)

    for synset in wn.synsets(a, wn.ADJ):
        a_sets.append(synset)
    
    for synset in wn.synsets(b, wn.ADJ):
        b_sets.append(synset)

    for synset in wn.synsets(a, wn.ADV):
        a_sets.append(synset)
    
    for synset in wn.synsets(b, wn.ADV):
        b_sets.append(synset)
    
    for a_set in a_sets:
        for b_set in b_sets:
            sim = a_set.path_similarity(b_set)
            if not sim:
                continue
            # print(sim)
            if shortest_path is None:
                shortest_path = sim
            elif sim < shortest_path:
                shortest_path = sim
    

    return shortest_path

ranking = {}
for pair in pairs:
    ranking[pair] = similarity(pair[0], pair[1])

for item in sorted(ranking.items(), key=lambda x:x[1]):
    print(item)