# coding=utf8
import os
from bs4 import BeautifulSoup
import requests
import urllib3

BASE_URL = 'http://www.shangdejy.com'
content = requests.get(BASE_URL + '/SiteFiles/Inner/page.aspx?s=1').content.decode('utf8')
bs = BeautifulSoup(content, 'html.parser')
'''img_tags = bs.find_all('img')
img_link = []
for each in img_tags:
    img_link.append(str(each).split('src="')[1].split('"')[0])
for each in img_link:
    raw_img = requests.get(BASE_URL + each).content
    file_name = each.split('/')[len(each.split('/')) - 1]
    with open(os.getcwd() + '/' + file_name, 'wb') as f:
        f.write(raw_img)
        f.close()'''
news_title = []
news_links = []
div = str(bs.find_all('div', class_='school_news', ))
bs2 = BeautifulSoup(div, 'html.parser')
news_tags = bs2.find_all('a')
for each in news_tags:
    news_title.append(str(each).split('>')[1].replace('</a', ''))
    news_links.append(str(each).split('href="')[1].split('"')[0])
news_links = news_links[1:]
news_title = news_title[1:]
index = 0
HTML_TEMPLATE = requests.get('https://raw.githubusercontent.com/leon332157/sd_spyder/master/raw_html.html').content
for each in news_links:
    each = each.replace(';', '').replace('amp', '')
    wx_link = requests.get(BASE_URL + each).url
    file_name = each.split('/')[len(each.split('/')) - 1]
    with open(os.getcwd() + '/' + str(news_title[index]) + '.html', 'w') as f:
        html = HTML_TEMPLATE.replace('{url}', wx_link)
        f.write(html)
        f.close()
    index += 1
print('完成！')
