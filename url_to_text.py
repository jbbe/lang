#!/usr/bin/python3
import sys, re
from urllib import request
from bs4 import BeautifulSoup

#2.8

def download_url(url):
    return request.urlopen(url).read().decode('utf8')

# start = raw.find("PART I")
# end = raw.rfind("End of Project Gutenberg's Crime")
# raw = raw[start:end]
# tokens = word_tokenize(raw)
# text = nltk.Text(tokens)
# sents = nltk.sent_tokenize(raw)
# pprint.pprint(sents[:30])

def main():
    raw = download_url(sys.argv[1])
    pretty = BeautifulSoup(raw, 'html.parser').get_text()
    # regex = re.compile(".#?\{.*?\}")
    # result = re.findall(regex, pretty)

    print('first', pretty[-200:])
    pretty = re.sub(r"([\{(\/\*)]).*?([\}(\*\/)])", "", pretty)
    pretty = re.sub(r"\{.*?\{", "", pretty)
    print('post', pretty[-200:])

if __name__ == '__main__':
    main()