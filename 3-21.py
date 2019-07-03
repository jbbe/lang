import nltk, re
from bs4 import BeautifulSoup
from urllib import request
# dictionary = open('/usr/share/dict/words').read()

# # ham = open('/Users/jbbe/interesa/txt_books/hamlet.txt').read().strip()

# uniq = [word for word in ham if word not in dictionary]

# print(uniq)

def download_url(url):
    return request.urlopen(url).read().decode('utf8')


def unknown(url):
    txt = download_url(url)
    words = set(re.findall(r'[a-z]+', txt))
    dictionary = nltk.corpus.words.words()
    return [word for word in words if word not in dictionary]

def extract(url):
    txt = download_url(url)
    pretty = BeautifulSoup(txt, 'html.parser').get_text()
    pretty = re.sub(r"([\{(\/\*)]).*?([\}(\*\/)])", "", pretty)
    pretty = re.sub(r"\{.*?\}", "", pretty)
    pretty = re.sub(r"\{.*?\(.*?\)\};", "", pretty)
    return pretty
    
# print(unknown('http://shakespeare.mit.edu/hamlet/full.html'))
# print(unknown("https://stackoverflow.com/questions/39536767/lazycorpusloader-object-is-not-iterable"))

print(extract('http://news.bbc.co.uk/'))