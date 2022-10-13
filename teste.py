import json
<<<<<<< HEAD


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

=======

nojson = '{"number": "Nilton Jr", "name": "testenilton", "unity": "Nova Iguaçu", "sector": "TI"}'



outro = json.loads(nojson)
print(type(outro))
for jn in outro:
    print(jn)
>>>>>>> 59384c64e6b6ae8aa263218f5653667530072037
