import nltk, re
from urllib import request

url = 'https://en.wikipedia.org/wiki/Franz_Kafka'
plain = request.urlopen(url).read().decode('utf8')
print(plain[:100])
clean = re.sub(r'<script [*] />', "", plain)
clean = re.sub(r'<.*?>', "", plain)
clean = re.sub(r'\s[\s]+', " ", clean)
clean = re.sub(r'\(\{[.*]\}\);', "", clean)
clean = re.sub(r'[{\[][.*][}\]]', "", clean)
clean = re.sub(r'{}', "", clean)
print(clean)