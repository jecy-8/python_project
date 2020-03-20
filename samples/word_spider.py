#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


URL = 'https://tool.lu/timestamp'
with open('/Users/jecy/Documents/python/test/spider_words.txt', "a") as f:
    for i in range(10):
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        for note in soup.find_all(class_ = 'note-container'):
            word = note.text.strip()
            f.write(word)
            f.write('\n')
            print(i, note.text)
        if i % 10 == 0:
            f.flush()
