import nltk, re


ham = open('/Users/jbbe/interesa/txt_books/hamlet.txt').read().strip() + "no i don't and never will"

wh_pattern = r'(?x) do|n\'t'
# qs = nltk.regexp_tokenize(text, wh_pattern)
toked = nltk.regexp_tokenize(ham, wh_pattern)
# print(ham)
print(toked)