## find()
# import requests
# from bs4 import BeautifulSoup
# import bs4

# def getHtml(url, my):
#     try:
#         r = requests.get(url, timeout=30, headers = my)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#         print('爬取失败')

# def Fillcase(html, movielist):
#     soup = BeautifulSoup(html, 'html.parser')
#     for divs in soup.find('ol').children: #观察源代码可知，ol包含了所有的电影信息
#         if isinstance(divs, bs4.element.Tag):
#             nameli = divs('span') #电影名包含在span中
#             movielist.append(nameli[0].string)

# def show(num, movielist):
#     for i in range(num):
#         print(movielist[i])

# def master():
#     url = 'https://movie.douban.com/top250'
#     my = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
#     html = getHtml(url, my)
#     movielist = []
#     Fillcase(html, movielist)
#     show(20, movielist)

# master()

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
    for i in range(num):
        print(movielist[i])

def starcase(html, starlist, num):
    soup = BeautifulSoup(html, 'html.parser')
    for ps in soup.find_all('div', class_ = 'star'):
        starlis = ps('span') 
        starlist.append(starlis[1].string)
    for i in range(num):
        print(starlist[i] + '分')

def quotecase(html, quotelist, num):
    soup = BeautifulSoup(html, 'html.parser')
    for ps in soup.find_all('p', class_ = 'quote'):
        quotelis = ps('span') 
        quotelist.append(quotelis[0].string)
    for i in range(num):
        print(quotelist[i])

def version():
    print('Getdouban-2.1')

url = 'https://movie.douban.com/top250'
my = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
html = getHtml(url, my)
quotelist = []
movielist = []
starlist = []

print('1.英文名' + '2.其他译名' + '3.是否可播放' + '4.演员' + '5.时间地区和标签' + '6.评分' + '7.经典语录' + '8.提交并显示版本')
choose = ['0']
count = eval(input('您共需要几项功能：'))
for i in range(count):
    choose.append(input('请选择你需要的功能：'))
num = eval(input('请输入要显示的电影数量'))
if '0' in choose:
    moviecase(html, movielist, num)

if '6' in choose:
    starcase(html, starlist, num)

if '7' in choose:
    quotecase(html, quotelist, num)