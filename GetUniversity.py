import requests
from bs4 import BeautifulSoup
import bs4
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser") #指定Beautiful的解析器为“html.parser”
    #通过搜索网页源代码发现，大学排名的具体信息保存在 tbody 标签中
    for trs in soup.find('tbody').children: # .find是搜索并只返回一个结果；.children是儿子节点
        # isinstance:判断一个对象是否是一个已知的类型，类似于type()
        # type()不考虑子类是父类的一种类型，不考虑继承关系
        # isinatance()认为子类是父类的一种类型，考虑继承关系
        # bs4.element.Tag
        # bs4是包，element是模块，Tag是类名
        # [tag是‘bs4.element.Tag’的实例对象，或者说tag的数据类型是bs4.element.Tag]
        # isinstance(object, classinfo)其中object是实例对象，classinfo可以是直接或间接类名、基本类型或者由它们组成的元组。
        # [使用方法：如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False。]
        if isinstance(trs, bs4.element.Tag): 
            tds = trs('td') #？
            ulist.append([tds[0].string, tds[1].string, tds[3].string]) # ？
 
def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
     
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs
main()