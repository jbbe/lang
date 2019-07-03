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