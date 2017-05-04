import requests
from bs4 import BeautifulSoup

import json
import os

BASE_URL = "https://www.packtpub.com"
FREE_LEARNING_PATH = "/packt/offers/free-learning"
#https://www.packtpub.com/freelearning-claim/21460/21478
# 'packtpub.json' config defaults
username = ''
password = ''

home_dir = os.path.expanduser('~')

with open(home_dir + "/packtpub.json") as json_config:
    credentials = json.load(json_config)
    username = credentials['user']['name']
    password = credentials['user']['password']

headers = {'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 9202.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.146 Safari/537.36'}

data = {'email': username, 
        'password': password, 
        'op': 'Login', 
        'form_build_id': 'form-a4f21aad8abbce3e5fb251a7f820c806',
        'form_id': 'packt_user_login_form'}

FREE_LEARNING_URL = BASE_URL + FREE_LEARNING_PATH

r = requests.get(FREE_LEARNING_URL, headers=headers)
print(r)

p = requests.post(FREE_LEARNING_URL, headers=headers, data=data)
print(p)

cookies = p.cookies
print(cookies)
#r = requests.get(FREE_LEARNING_URL, headers=headers, cookies=cookies)
#print(r.text)
soup = BeautifulSoup(r.text, 'html.parser')
links = [a.attrs.get('href') for a in soup.select('div.free-ebook a[href^=]')]

print(links)
print(BASE_URL + links[0])

r = requests.get(BASE_URL + links[0], headers=headers, cookies=cookies)
print(r)
