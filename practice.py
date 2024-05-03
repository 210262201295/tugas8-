import requests

api_key = '1c5e8609-9c86-49c3-b53e-34907aa5a581'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)

for definition in definitions:
    print(definition)