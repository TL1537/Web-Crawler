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
    soup = BeautifulSoup(html, 'html.parser') # soup解析后的结果和html原本的结果在于结构的差异，内容上并没有变化
    htm = soup.find('ol', class_ = 'grid_view')
    # <tag>(..) 等价于 <tag>.find_all(..)
    # soup(..) 等价于 soup.find_all(..)
    # for li in htm.find_all('li'):
    for li in htm('li'):
        try:
            ID = li.find('em', class_ = '').text
            name = li.find('span', class_ = 'title').text
            # href = li.find('a').get('href') # href是个字符串 正确
            # href = li.a['href'] # href是个字符串 正确
            href = li.a.get('href') # href是个字符串 正确
            # href = li.a('href') # href是个空列表 错误
            # href = li.a.find('href') # href是空类型nonetype 错误
            # href = li.a.find(['href']) # href是空类型nonetype 错误
            # href = li.a.find_all('href') # href是个空列表 错误
            # href = li.a.find_all(['href'])  # href是个空列表(却是resultset值) 错误
            star_comment = li.find('div', class_ = 'star').text.replace('\n', '   ')#.strip()
            # quote = li.find('p', class_ = 'quote').text.replace('\n', '') # 删除换行符.replace('\n', '')，删除空格.strip()
        except:
            quote = '暂无经典语录'
        print('{0:>5}{1:>20}{2:>50}{3:^40}'.format(ID, name, href, star_comment))# {4:>40}, quote, chr(12288)

def main():
    print('{0:^5}\t\t{1:^20}{2:^50}{3:^40}'.format('排名', '电影名', '链接', '评分和评论'))# \t{4:^40}, '经典语录', chr(12288)
    url = 'https://movie.douban.com/top250?start={}&filter='
    urls = [url.format(num * 25) for num in range(10)]
    for i in urls:
        html = getHTML(i)
        filter(html)
        time.sleep(1)

main()