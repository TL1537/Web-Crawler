# find_all()
import requests
from bs4 import BeautifulSoup
import bs4

def getHtml():
    url = 'https://movie.douban.com/top250'
    my = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    try:
        r = requests.get(url, timeout=30, headers = my)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败')

def moviecase(movielist):
    for divs in soup.find_all('div', class_ = 'hd'):
        movieli = divs('span') 
        movielist.append(movieli[0].string)

def foreign_moviecase(foreign_movielist):
    for divs in soup.find_all('div', class_ = 'hd'):
        for acs in divs.find_all('a', class_ = ''):
            foreign_movieli = acs('span')
        if len(foreign_movieli) == 3:
            foreign_movielist.append((foreign_movieli[1].string)[3:])
        else:
            foreign_movielist.append('无源外语名')

def other_moviecase(other_movielist):
    for divs in soup.find_all('div', class_ = 'hd'):
        for acs in divs.find_all('a', class_ = ''):
            other_movieli = acs('span')
        if len(other_movieli) == 3:
            other_movielist.append((other_movieli[2].string)[3:])
        else:
            other_movielist.append((other_movieli[1].string)[3:])

def playcase(playlist):
    for divs in soup.find_all('div', class_ = 'hd'):
        playli = divs('span')
        if len(playli) == 4:
            playlist.append((playli[3].string))
        else:
            playlist.append('[不可播放]')
def starcase(starlist):
    for ps in soup.find_all('div', class_ = 'star'):
        starlis = ps('span') 
        starlist.append(starlis[1].string)

def quotecase(quotelist):
    for ps in soup.find_all('p', class_ = 'quote'):
        quotelis = ps('span') 
        quotelist.append(quotelis[0].string)

def version():
    print('Getdouban-2.5')


html = getHtml()
soup = BeautifulSoup(html, 'html.parser')
quotelist = []
movielist = []
starlist = []
foreign_movielist = []
other_movielist = []
playlist = []


print('1.源外语名 ' + '2.其他译名 ' + '3.是否可播放 ' + '4.演员 ' + '5.时间地区和标签 ' + '6.评分 ' + '7.经典语录 ' + '8.显示版本')
choose = ['0']
count = eval(input('您共需要几项功能：'))
for i in range(count):
    choose.append(input('请选择你需要的功能：'))
num = eval(input('请输入要显示的电影数量：'))

#------------------------
# tempcount = '1'
# for i in range(count):
#     choose.append(input('请选择你需要的第' + tempcount + '项功能：'))
#     int(tempcount)
#     tempcount = tempcount + 1
#     str(tempcount)
#-----------------------


if '0' in choose:
    print('电影名', end='')
if '1' in choose:
    print('源外语名', end='')
if '2' in choose:
    print('其他译名', end='')
if '3' in choose:
    print('能否播放', end='')
if '6' in choose:
    print('评分', end='')
if '7' in choose:
    print('经典语录')

for time in range(num):
    if '0' in choose:
        moviecase(movielist)
        print(movielist[time] + ' ', end='')

    if '1' in choose:     
        foreign_moviecase(foreign_movielist)
        print(foreign_movielist[time] + ' ', end='')

    if '2' in choose:        
        other_moviecase(other_movielist)
        print(other_movielist[time] + ' ', end='')

    if '3' in choose:        
        playcase(playlist)
        print(playlist[time] + ' ', end='')

    if '6' in choose:        
        starcase(starlist)
        print(starlist[time] + '分 ', end='')

    if '7' in choose:        
        quotecase(quotelist)
        print(quotelist[time] + ' ')

if '8' in choose:
    version()

    