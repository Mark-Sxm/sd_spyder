# coding=utf8
import os
from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://www.shangdejy.com'  # 初始网址
content = requests.get(BASE_URL + '/SiteFiles/Inner/page.aspx?s=1').content.decode('utf8')  # 主义
bs = BeautifulSoup(content, 'html.parser')  # 实例化bs类
'''img_tags = bs.find_all('img')
img_link = []
for each in img_tags:
    img_link.append(str(each).split('src="')[1].split('"')[0])  # 找到图片链接
for each in img_link:
    raw_img = requests.get(BASE_URL + each).content  # 获取图片 ！！！这里获取到的是bytes
    file_name = each.split('/')[len(each.split('/')) - 1]  # 根据请求的链接设置图片文件名
    with open(os.getcwd() + '/' + file_name, 'wb') as f:  # 需要以bytes写入模式打开
        f.write(raw_img)  # 写入
        f.close()  # 关闭'''
news_title = []  # 初始化空列表
news_links = []  # 初始化空列表
div = str(bs.find_all('div', class_='school_news', ))  # 找到news标签
bs2 = BeautifulSoup(div, 'html.parser')  # 实例化bs类
news_tags = bs2.find_all('a')  # 找到a标签，包含了标题和链接
for each in news_tags:
    news_title.append(str(each).split('>')[1].replace('</a', ''))  # 提取标题
    news_links.append(str(each).split('href="')[1].split('"')[0])  # 提取链接
news_links = news_links[1:]  # 去除第一个不相关的图片链接
news_title = news_title[1:]  # 去除第一个不相关的图片标题
index = 0
HTML_TEMPLATE = str(
    requests.get('https://raw.githubusercontent.com/leon332157/sd_spyder/master/html_template.html').text)  # JS的重定向模板
for each in news_links:
    each = each.replace(';', '').replace('amp', '')  # 多出来的amp...
    wx_link = requests.get(BASE_URL + each).url  # 获取公众号链接
    file_name = each.split('/')[len(each.split('/')) - 1]  # 保存文件名，标题的索引是index
    with open(os.getcwd() + '/' + str(news_title[index]) + '.html', 'w') as f:
        html = HTML_TEMPLATE.replace('{url}', wx_link)  # 插入微信公众号链接
        f.write(html)  # 写入
        f.close()  # 关闭
    index += 1  # 每次保存完加一个索引
print('完成！')
