# coding:utf-8
import requests
import time
import gevent
import re
import os
import random
from lxml import etree
from gevent import monkey
from bs4 import BeautifulSoup
from urllib import parse
#monkey.patch_all(select=False)

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '__cfduid=d820fcba1e8cf74caa407d320e0af6b5d1518500755; UM_distinctid=1618db2bfbb140-060057ff473277-4323461-e1000-1618db2bfbc1e4; ctrl_time=1; CNZZDATA1272873873=2070014299-1518497311-https%253A%252F%252Fwww.baidu.com%252F%7C1518507528; yjs_id=69163e1182ffa7d00c30fa85105b2432; jieqiVisitTime=jieqiArticlesearchTime%3D1518509603'
    }
IPs = [
        {'HTTPS': 'https://115.237.16.200:8118'},
        {'HTTPS': 'https://42.49.119.10:8118'},
        {'HTTPS': 'http://60.174.74.40:8118'}
    ]


# 设置小说存储目录
def setDir():
    if 'Noval' not in os.listdir('./'):
        os.mkdir('./Noval')


def getNoval(url, id):
    IP = random.choice(IPs)
    res = requests.get(url, headers=headers, proxies=IP)
    res.encoding = 'GB18030'
    html = res.text.replace('&nbsp;', ' ')  # 替换掉这个字符 换成空格~ 意思是一样的
    page = etree.HTML(html)
    content = page.xpath('//div[@id="content"]')
    ps = page.xpath('//div[@class="bookname"]/h1')
    if len(ps) != 0:
        s = ps[0].text + '\n'
        s = s + content[0].xpath("string(.)")
        with open('./Noval/%d.txt' % id, 'w', encoding='gb18030', errors='ignore') as f:
            f.write(s)


def getContentFile(url):

    IP = random.choice(IPs)
    res = requests.get(url, headers=headers, proxies=IP)
    res.encoding = 'GB18030'
    page = etree.HTML(res.text)
    #其实页面标签为 info的
    bookname = page.xpath('//div[@id="info"]/h1')[0].xpath('string(.)') 
    dl = page.xpath('//div[@id="list"]/dl/dd/a')
    splitHTTP = parse.urlsplit(url)
    url = splitHTTP.scheme + '://' + splitHTTP.netloc
    return list(map(lambda x: url + x.get('href'), dl)), bookname


def BuildGevent(baseurl):
    content, bookname = getContentFile(baseurl)  # version2
    steps = 20
    length = len(content)
    
    count = 0
    name = "%s.txt" % bookname
    while (count - 1) * steps < length:
        WaitigList = [gevent.spawn(getNoval, content[i + count * steps], i + count * steps) for i in range(steps) if
                      i + count * steps < length]
        gevent.joinall(WaitigList)      #将等待列表里面的 进程全部加入
        # 将生成的单个章节的txt文件 排好顺序
        NovalFile = list(filter(lambda x: x[:x.index('.')].isdigit(), os.listdir('./Noval')))
        NovalFile.sort(key=lambda x: int(re.match('\d+', x).group()))

        #将单个章节的文件读取进来后删除源文件
        String = ''
        for dirFile in NovalFile:
            with open('./Noval/' + dirFile, 'r', encoding='gb18030', errors='ignore') as f:
                String = String + '\n' + f.read()
            os.remove('./Noval/%s' % dirFile)
        
        # 第一次需要新建文件 之后进行追加写文件
        if count == 0:
            with open('./Noval/' + name, 'w', encoding='gb18030', errors='ignore') as ff:
                ff.write(String)
        else:
            with open('./Noval/' + name, 'a', encoding='gb18030', errors='ignore') as ff:
                ff.write(String)
        count += 1


if __name__ == '__main__':
    starttime = time.time()
    setDir()
    url = 'http://www.biquge.com.tw/3_3711/'
    BuildGevent(url)
    endtime = time.time()
    print("Total use time: %.6f" % (endtime - starttime))
