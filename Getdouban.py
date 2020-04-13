# find()
import requests
from bs4 import BeautifulSoup
import bs4

def getHtml(url, my):
    try:
        r = requests.get(url, timeout=30, headers = my)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败')

def Fillcase(html, movielist):
    soup = BeautifulSoup(html, 'html.parser')
    for divs in soup.find('ol').children: #观察源代码可知，ol包含了所有的电影信息
        if isinstance(divs, bs4.element.Tag):
            nameli = divs('span') #电影名包含在span中
            movielist.append(nameli[0].string)

def show(num, movielist):
    for i in range(num):
        print(movielist[i])

def master():
    url = 'https://movie.douban.com/top250'
    my = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    html = getHtml(url, my)
    movielist = []
    Fillcase(html, movielist)
    show(20, movielist)

master()