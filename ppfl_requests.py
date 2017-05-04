import requests
import json
import os

BASE_URL = "https://www.packtpub.com/packt/offers/free-learning"

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

r = requests.get(BASE_URL, headers=headers)
print(r)

p = requests.post(BASE_URL, headers=headers, data=data)
print(p)

cookies = p.cookies
print(cookies)
r = requests.get(BASE_URL, headers=headers, cookies=cookies)
#print(r.text)

