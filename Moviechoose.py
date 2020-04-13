# find_all()
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

def moviecase(html, movielist, num):
    soup = BeautifulSoup(html, 'html.parser')
    for divs in soup.find_all('div', class_ = 'hd'):
        movieli = divs('span') 
        movielist.append(movieli[0].string)

def starcase(html, starlist, num):
    soup = BeautifulSoup(html, 'html.parser')
    for ps in soup.find_all('div', class_ = 'star'):
        starlis = ps('span') 
        starlist.append(starlis[1].string)

def quotecase(html, quotelist, num):
    soup = BeautifulSoup(html, 'html.parser')
    for ps in soup.find_all('p', class_ = 'quote'):
        quotelis = ps('span') 
        quotelist.append(quotelis[0].string)

def version():
    print('Getdouban-2.2')

url = 'https://movie.douban.com/top250'
my = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
html = getHtml(url, my)
quotelist = []
movielist = []
starlist = []

print('1.英文名 ' + '2.其他译名 ' + '3.是否可播放 ' + '4.演员 ' + '5.时间地区和标签 ' + '6.评分 ' + '7.经典语录 ' + '8.显示版本')
choose = ['0']
count = eval(input('您共需要几项功能：'))
for i in range(count):
    choose.append(input('请选择你需要的功能：'))
num = eval(input('请输入要显示的电影数量'))
for time in range(num):
    if '0' in choose:
        moviecase(html, movielist, num)
        print(movielist[time])

    if '6' in choose:
        starcase(html, starlist, num)
        print(starlist[time] + '分')

    if '7' in choose:
        quotecase(html, quotelist, num)
        print(quotelist[time])

    if '8' in choose:
        version()