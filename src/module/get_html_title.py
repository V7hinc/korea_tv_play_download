#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""
    @Author:V7hinc
    @Datetime:2021/11/15 16:06
    @Software:PyCharm
    @Filename:get_html_title.py
"""

# 正式代码
# pip3 install beautifulsoup4
from bs4 import BeautifulSoup
import requests


def get_html_title(url):
    root_url = url.replace('://', ':%%', 1).split('/', 1)[0].replace(':%%', '://', 1)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    # s = soup.prettify()
    # print(s)
    html_info = {'title': soup.title.get_text(), 'last_episode': None, 'next_episode': None}
    for item in soup.find_all("a"):
        if item.get_text() == "下集":
            html_info['next_episode'] = f'{root_url}{item.get("href")}'
        elif item.get_text() == "上集":
            html_info['last_episode'] = f'{root_url}{item.get("href")}'
    return html_info


if __name__ == '__main__':
    a = get_html_title('https://www.kan.cc/play/2563-0-0.html')
    print(a)
