import nltk, re
corpus_root = '/Users/jbbe/interesa/txt_books'

def load(f):
    with open(f) as file:
        return file.read()

txt = load('/Users/jbbe/interesa/txt_books/putas_asesinas.txt')

def punc_tokenizer(txt):
    pattern = r'''(?x)
        ,
        | \.\.\.
        | \.
        | ,
    '''
    return nltk.regexp_tokenize(txt, pattern)

# print(txt)
# print(punc_tokenizer(txt))
txt = txt + "Ok what the fuck is this money $5.00 or 6.69 or $6.69 it happened 6/15/2019 or maybe it 3/8/99"
def b_tokenizer(txt):
    pattern = r'''(?x)
         \$[\d\.]+
        | \d{,2}\/\d{,2}\/\d{2,4}
        | ^[A-Z]{1}[a-z]+
    '''
    return nltk.regexp_tokenize(txt, pattern)

print(b_tokenizer(txt))

# with open('/Users/jbbe/interesa/txt_books/amuleto.txt', 'w+') as f:
    # f.write(amu_clean)

# amu_clean = re.sub(r"Página \d+ de \d+", "", txt)
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']

result = [(word, len(word)) for word in sent]
print(result)

raw = "Prine's stuff is pure Proustian existentialism. \t Midwestern mindtrips to the nth degree. \t \t \t And he writes \n beautiful songs. \n \t I remember when Kris Kristofferson first brought him on the scene. All that stuff about Sam Stone the soldier junky daddy and Donald and Lydia, where people make love from ten miles away. Nobody but Prine could write like that. If I had to pick one song of his, it might be Lake Marie. I don't remember what album that's on,"

# 2-12
for letter in raw:
    print(letter)

# 2- 13
# split() will split on all spaces including \t and \n
# split(' ') will split only on single white spaces

words = raw.split()
# Sorted(ist) returns a sorted copy
# .sort() sorts the lsit in place

