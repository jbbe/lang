import nltk, re

def find_line_split(text):
    return re.findall(r'[A-za-z]+-\n[a-z]+', text)

def remove_line_break(text):
    return re.sub(r'-\n', '-', text)
        

alas = """Alas, poor Yorick! I knew him, Horatio: a fellow
of infinite jest, of most excellent fancy: he hath
borne me on his back a thousand times; and now, how
abhorred in my imagination it is! my gorge rims at
it. Here hung those lips that I have kissed I know
not how oft. Where be your gibes now? your
gambols? your songs? your flashes of merr-\niment,
that were wont to set the table on a roar? Not one
now, to mock your own grinning? quite chap-fallen?
Now get you to my lady's cha-\nmber, and tell her, let
her paint an inch thick, to this favour she must
come; make her laugh at that. """


print(find_line_split(alas))
print(remove_line_break(alas))