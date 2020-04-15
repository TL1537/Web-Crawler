import requests

url = 'https://m.ip138.com/iplookup.asp?ip='
my = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

def search(ip):
    try:
        r = requests.get(url + ip, headers = my)
        print(r.status_code)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        print(r.text[-2000:-1000])
    except:
        print('爬取失败')
        
ip = input('请输入要查询的IP地址：')
search(ip)
