from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

import os
import time
import json

# 'packtpub.json' config defaults
username = ''
password = ''

home_dir = os.path.expanduser('~')
#print("*** HOME_DIR: {}".format(home_dir))

with open(home_dir + "/packtpub.json") as json_config:
    credentials = json.load(json_config)
    username = credentials['user']['name']
    password = credentials['user']['password']

driver = webdriver.Firefox()
driver.get('https://www.packtpub.com/packt/offers/free-learning')
assert "Free Learning" in driver.title

try:
    # stash the book title to check that we saved it
    book_title = driver.find_element_by_class_name('dotd-title').text

    free_book_submit = driver.find_element_by_class_name('book-claim-token-inner')
    free_book_submit.click()

    #print("*** BOOK TITLE: {}".format(book_title))
    
    # have to access hidden elements this way, since we're unable to send keys to elements
    driver.execute_script("document.getElementById('email').value='{}'".format(username))
    driver.execute_script("document.getElementById('password').value='{}'".format(password))
    driver.execute_script("document.getElementById('edit-submit-1').click()")
    free_book_submit = driver.find_element_by_class_name('book-claim-token-inner')
    free_book_submit.click()

    #https://www.packtpub.com/account/my-ebooks
    # refresh after the redirect
    driver.get(driver.current_url)

    account_ebooks = driver.find_element_by_id('account-right-content')

    #print("*** ACCOUNT EBOOKS: {}".format(account_ebooks.text))

    if book_title in account_ebooks.text:
        print("*** SUCCESSFULLY ADDED BOOK - {} ***".format(book_title))
    else:
        print("*** FAILED TO ADD BOOK  ***")
finally:
    driver.close()

