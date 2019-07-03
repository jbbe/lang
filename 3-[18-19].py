import nltk

text = ''
with open('/Users/jbbe/interesa/txt_books/hamlet.txt') as f:
    text = f.read()

wh_pattern = r'(?x) [wW]h[a-z]+'
qs = nltk.regexp_tokenize(text, wh_pattern)
# print(qs, len(qs))

word_list_raw = open('list.txt').readlines()
word_list = []
word_list = [[line.split()[0], int(line.split()[1])] for line in word_list_raw]
# for line in word_list_raw:
    # word_list.append([line.split()[0], int(line.split()[1])])
print(word_list)