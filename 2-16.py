import nltk
from nltk.corpus import brown

def lexical_diversity(my_text_data):
     word_count = len(my_text_data)
     vocab_size = len(set(my_text_data))
     diversity_score = vocab_size / word_count
     return diversity_score

scores = {}
for cat in brown.categories():
    scores[cat] = lexical_diversity(brown.words(categories=cat))
    print(cat, (' '*(15-len(cat))), lexical_diversity(brown.words(categories=cat)))

