import requests
from bs4 import BeautifulSoup
import time

def getHTML(url):
    my = {'user-agent':'Mozilla/5.0'}
    try:
        r = requests.get(url, headers = my)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('爬取失败')

def filter(html):
    soup = BeautifulSoup(html, 'html.parser')
    htm = soup.find('ol', class_ = 'grid_view')
    for li in htm.find_all('li'):
        try:
            ID = li.find('em', class_ = '').text
            name = li.find('span', class_ = 'title').text
            href = li.a['href']
            quote = li.find('p', class_ = 'quote').text.replace('\n', '') # 删除换行符.replace('\n', '')，删除空格.strip()
        except:
            quote = '暂无经典语录'
        print('{0:>5}{1:>20}{2:>50}{3:>40}'.format(ID, name, href, quote, chr(12288)))

def main():
    print('{0:^5}\t\t{1:^20}{2:^50}\t{3:^40}'.format('排名', '电影名', '链接', '经典语录', chr(12288)))
    url = 'https://movie.douban.com/top250?start={}&filter='
    urls = [url.format(num * 25) for num in range(10)]
    for i in urls:
        html = getHTML(i)
        filter(html)
        time.sleep(1)

main()