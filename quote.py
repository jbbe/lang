#!/usr/bin/python3
# 3-20
import sys, re
from urllib import request
from bs4 import BeautifulSoup

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
    raw = download_url('https://www.eduro.com/')
    pretty = BeautifulSoup(raw, 'html.parser').get_text()
    start = pretty.find("Today's Quote of the Day")

    end = pretty.rfind('Also: Today\'s ')
    print(pretty[start+40:end].strip())

if __name__ == '__main__':
    main()