import requests

base_url = 'https://yande.re/'
user_input = input("Tag: ")
api_url = f'{base_url}post.json?tags={user_input}'

r = requests.get(api_url)

src = r.json()

for item in src:
    print(item['tags'])
    print(item['file_url'])
