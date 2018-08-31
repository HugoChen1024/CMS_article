# coding:utf-8
import requests
import time
from bs4 import BeautifulSoup

# url 池存储
url = "https://www.qu.la/book/12763/10664294.html"
base = url[:url.rindex('/') +1 ]
urls = [url]
first =True

for url in urls:
    req = requests.get(url)
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'html.parser')

    try:
        content = soup.find(id='content')
        title = soup.find(attrs={"class":"bookname"})
        title = title.find('h1').text
    except:
        break

    string = content.text.replace('\u3000', '').replace('\t', '').replace('\n', '').replace('\r', '').replace('『', '“')
    string = string.split('\xa0')
    string = list(filter(lambda x: x, string))
    for i in range(len(string)):
        string[i] = '    ' +string[i]
    
    string = '\n'.join(string)

    string = '\n'+ title +'\n \n' + string

    if first:
        first = False
        with open('./test/txt/1.txt', 'w') as f:
            f.write(string)
    else:
        with open('./test/txt/1.txt', 'a') as f:
            f.write(string)

    print(url+'  '+title+' 写入完成')

    next_ = soup.find(attrs={"class": "next"})
    next_url = base + next_['href']
    urls.append(next_url)
    #time.sleep(1)  # 别访问的太快了..担心被禁hhh也别访问的太死板了










