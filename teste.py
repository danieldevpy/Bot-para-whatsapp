import json

nojson = '{"number": "Nilton Jr", "name": "testenilton", "unity": "Nova Iguaçu", "sector": "TI"}'



outro = json.loads(nojson)
print(type(outro))
for jn in outro:
    print(jn)