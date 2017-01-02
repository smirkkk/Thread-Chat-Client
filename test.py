import requests
import json

b = requests.get('http://goo.gl/8Leiyi')

#print(b.text)

b.json()['glossary']['title']
c = json.loads(b.text)

print(c)

c['glossary']['body'] = '123'

print(c)
print(b.json()['glossary']['title'])