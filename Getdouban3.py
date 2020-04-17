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
    movie_list = soup.find('ol', class_ = 'grid_view') #将网页数据范围缩小，得到的结果movie_list是列表，但此列表长度为1！
    for li in movie_list.find_all('li'):
        try:
            ID = li.find('em', class_ = '').text
            name = li.find('span', class_ = 'title').text
            #taga = li('a') #列表，存入了50个链接
            taga = li.a #第一个a标签所包含的所有内容
            href = taga['href']
            play = li.find('span', class_ = 'playable').text
            player = li.find('p', class_ = '').text
            quote = li.find('p', class_ ='quote').text
        except:
            quote = ''
            play = '[不可播放]'
            player = '暂无'
        print('排名：{}，名字：{}，链接：{}，播放：{}，演员：{}，经典语录{}'.format(ID, name, href, play, player, quote))
            

def main():
    url = 'https://movie.douban.com/top250?start={}&filter='
    urls = [url.format(num * 25) for num in range (10)]
    for i in urls:
        html = getHTML(i)
        filter(html)
        time.sleep(1)
main()