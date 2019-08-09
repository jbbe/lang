import nltk, re

ham = open('/Users/jbbe/interesa/txt_books/hamlet.txt').read().strip() 

def to_hacker(text):
    text = re.sub(r"e", "3", text)
    text = re.sub(r"i", "1", text)
    text = re.sub(r"o", "0", text)
    text = re.sub(r"l", "|", text)
    text = re.sub(r"\ss", " 5", text)
    text = re.sub(r"s", "$", text)
    # text = re.sub(r"\.", "5w33t!", text)
    text = re.sub(r"ate", "8", text)
    return text

def to_pig_latin_word(word):
    if len(word) == 0:
        return word
    letter = word[0].lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return word + 'ay'
    upper = False
    if word[0].isupper():
        upper = True
    place = 0
    word = word.lower()
    for letter in word:
        if letter == 'q':
            place += 2
            break
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            break
        if letter == 'y':
            if place == len(word) - 1:
                break
            nletter = word[place+1]
            if nletter == 'a' or nletter == 'e' or nletter == 'i' or nletter == 'o' or nletter == 'u':
                place += 1
                continue
            else:
                break
        place += 1
    if upper:
       return (word[place:] + word[:place] + 'ay').capitalize()

    return word[place:] + word[:place] + 'ay'


def to_pig_latin_text(text):
    words = nltk.word_tokenize(text)
    return [to_pig_latin_word(word) for word in words]

alas = """Alas, poor Yorick! I knew him, Horatio: a fellow
of infinite jest, of most excellent fancy: he hath
borne me on his back a thousand times; and now, how
abhorred in my imagination it is! my gorge rims at
it. Here hung those lips that I have kissed I know
not how oft. Where be your gibes now? your
gambols? your songs? your flashes of merriment,
that were wont to set the table on a roar? Not one
now, to mock your own grinning? quite chap-fallen?
Now get you to my lady's chamber, and tell her, let
her paint an inch thick, to this favour she must
come; make her laugh at that. """

print(to_hacker(alas))


# print(to_pig_latin_text(alas))
# print(to_pig_latin_word('style'))