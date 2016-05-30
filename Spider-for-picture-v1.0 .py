'''
这是一个用Beautifulsoup库做的python爬虫
用来爬去蜂鸟网图片：http://tu.fengniao.com/79/
只要根据具体情况改一改：
line14的range的范围，
line15的url，
line24的具体网站的'/forum/8937924.html'即可
'''
#coding=utf-8
import requests, urllib, os
from bs4 import BeautifulSoup

ans = 1 #用来计数的变量

name = '' #相册名字初始化

for page in range(795, 807):
    url = 'http://bbs.fengniao.com/forum/pic/slide_101_8937924_80643' + str(page) + '.html'
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'}
    source_code = requests.get(url, headers=header)
    soup = BeautifulSoup(source_code.text, 'lxml')

    download_link = []

    for link in soup.find_all('a'):
        #获取相册标题
        if name == '':
            if link.get('href') == '/forum/8937924.html': #每个相册的forum都不同，根据具体来修改即可
                if link.get('title') == None:
                    pass
                else:
                    name = link.get('title')
                    图片保存路径
                    folder_path = 'D:\spider_things\\2016.5.30\\' + name + '\\'#一旦获得相册名称后就马上书写folder_path

        if link.get('class') == ['pictureDownload']:
            if link.get('href') == '': #如果是空页
                pass
            else:
                download_link.append(link.get('href'))

    #创建文件夹
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    #下载图片
    for each in download_link:
        try:
            urllib.urlretrieve(each, folder_path + str(ans) + '.jpg')
            print 'you have download ', ans , 'pic(s)'
            ans += 1
        except urllib.ContentTooShortError, e: #如果有些图片太大，下载不了的话，就跳过
            continue

