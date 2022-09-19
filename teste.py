import json


def testando(name, age=None, outro=None, city=None):
    print(name, age, outro, city)


info = str(input('digite os campos: '))
# some JSON:
transf = {info}

# parse x:
emjson = json.loads(info)

name = None
age = None
city = None

for chave in emjson:
    if chave == 'name':
        name = emjson[chave]
    elif chave == 'age':
        age = emjson[chave]
    elif chave == 'city':
        city = emjson[chave]

testando(name, age, city)
# the result is a Python dictionary:

