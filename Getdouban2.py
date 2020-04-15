import requests
from bs4 import BeautifulSoup
import bs4
import time

def getHTML(url):
    try:
        my = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url, headers = my)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text, r.status_code
    except:
        print('爬取失败')

def filter(html, pages, code):
    soup = BeautifulSoup(html, 'html.parser')
    print('第{}页的状态码为'.format(pages) + code)
    for divs in soup.find_all('div', class_ = 'hd'):
        tag = divs.find('a')
        name = tag.find(class_ = 'title').text
        herf = tag['href']    
        print(name, herf)
    print('==========================================================')

def main():
    pages = 0
    print('起床干活啦')
    url = 'https://movie.douban.com/top250?start={}&filter='
    urls = [url.format(num * 25) for num in range(10)]
    for i in urls:
        html = getHTML(i)[0]
        code = getHTML(i)[1]
        code = str(code)
        pages = pages + 1
        filter(html, pages, code)
    time.sleep(1)

main()
print('完事了，睡觉')