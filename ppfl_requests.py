import requests
from bs4 import BeautifulSoup

import json
import os

BASE_URL = "https://www.packtpub.com"
FREE_LEARNING_PATH = "/packt/offers/free-learning"
MY_BOOKS_PATH = "/account/my-ebooks"

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

session = requests.Session()

r = session.get(FREE_LEARNING_URL, headers=headers)
print(r)

p = session.post(FREE_LEARNING_URL, headers=headers, data=data)
print(p)

cookies = p.cookies
print(cookies)

soup = BeautifulSoup(r.text, 'html.parser')
book_title = soup.find('div', { 'class': 'dotd-title'}).find('h2').text.strip()
print(book_title)
#links = [a.attrs.get('href') for a in soup.select('div.free-ebook a[href^=]')]
link = soup.find('div', {'class': 'free-ebook'}).find('a').attrs.get('href')
print(link)

#print(links)
#print(BASE_URL + links[0])

r = session.get(BASE_URL + link, headers=headers, cookies=cookies)
print(r)

r = session.get(BASE_URL + MY_BOOKS_PATH, headers=headers, cookies=cookies)
print(r)

if book_title in r.text:
    print("*** SUCCESSFULLY ADDED BOOK - {} ***".format(book_title))
else:
    print("*** FAILED TO ADD BOOK ***")
