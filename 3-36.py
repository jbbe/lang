import nltk, re
# from nltk.book import text3

def to_lolcat(text):
    text = re.sub(r'earth', 'urf', text, flags=re.IGNORECASE)
    text = re.sub(r'God', 'Ceiling Cat', text, flags=re.IGNORECASE)
    text = re.sub(r'father', 'daddy-cat', text, flags=re.IGNORECASE)
    text = re.sub(r'daughter', 'dotter', text, flags=re.IGNORECASE)
    text = re.sub(r'kitten', 'kitteh', text, flags=re.IGNORECASE)
    text = re.sub(r'kitten', 'cat', text, flags=re.IGNORECASE)
    text = re.sub(r'mother', 'mom-kitteh', text, flags=re.IGNORECASE)
    text = re.sub(r'cow', 'moocow', text, flags=re.IGNORECASE)
    text = re.sub(r'people', 'pepples', text, flags=re.IGNORECASE)
    text = re.sub(r'sheep', 'sheepies', text, flags=re.IGNORECASE)
    text = re.sub(r'shepherds', 'shep-doods', text, flags=re.IGNORECASE)
    text = re.sub(r'sister', 'sisty-kitty', text, flags=re.IGNORECASE)
    text = re.sub(r'the', 'da', text, flags=re.IGNORECASE)
    text = re.sub(r'eat', 'nom', text, flags=re.IGNORECASE)
    text = re.sub(r'devil', 'Basement Cat', text, flags=re.IGNORECASE)
    text = re.sub(r'Jesus Christ', 'Happy Cat', text, flags=re.IGNORECASE)
    text = re.sub(r'Lord Jesus', 'Lord Happy', text, flags=re.IGNORECASE)
    new = re.sub(r'brother', 'Brutha', text, flags=re.IGNORECASE)
    return new

genesis = nltk.corpus.gutenberg.raw('bible-kjv.txt')

print(to_lolcat(genesis))