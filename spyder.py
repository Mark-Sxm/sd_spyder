# coding=utf8
import os
from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://www.shangdejy.com'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
content = requests.get(BASE_URL + '/SiteFiles/Inner/page.aspx?s=1', headers=HEADERS).content.decode('utf8')
bs = BeautifulSoup(content, 'html.parser')
img_tags = bs.find_all('img')
img_link = []
for each in img_tags:
    img_link.append(str(each).split('src="')[1].split('"')[0])
for each in img_link:
    raw_img = requests.get(BASE_URL + each, headers=HEADERS).content
    file_name = each.split('/')[len(each.split('/')) - 1]
    with open(os.getcwd() + '/' + file_name, 'wb') as f:
        f.write(raw_img)
        f.close()
print('完成！')
