from random import choice

string = "aehh "

res = ""
for i in range(500):
    res += choice(string)
res = res.split()
res = ' '.join(res)
print(res)