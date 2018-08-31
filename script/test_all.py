# coding:utf-8
import requests
import time
import gevent
import re
import os
import json
import pymysql
import random
from lxml import etree
from gevent import monkey
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime
from xlwt import *

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


def getOnePage(page_url):
    result = {}
    IP = random.choice(IPs)
    res =requests.get(page_url, headers=headers, proxies=IP)
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text, 'html.parser')

    # 替换掉这个字符 换成空格
    main_title= soup.select('.content_right h1')[0].text
    category = soup.select('.blog_post_details li')[0].text
    author = soup.select('.blog_post_details li')[1].text 
    date_time = soup.select('.blog_post_details li')[2].text 
    views = soup.select('.blog_post_details li')[3].text 

    # 将article 下面的p 标签下的文字组合成段落
    article = soup.select('.content_right p')
    article_text =' '.join([p.text.strip() for p in article[:-1]]) 

    #print(article_text)


    result['main_title']  = main_title
    result['date_time']  = date_time
    result['author']  = author
    result['article_text']  = article_text

    content = url_tmp+'\n' + main_title +'\n'+category +'    '+author +'    '+date_time +'    '+views+'\n' + article_text +'\n'

    with open('1.txt', 'a', encoding='gb2312', errors='ignore') as f:
        f.write(content)



    return result





if __name__ == '__main__':
    starttime = time.time()
    url = 'http://pmc.whu.edu.cn/Article/15633.html'

    base_url = url[:url.rindex('/') +1 ]

    url_count = 15633

    for num in range(url_count-1000,url_count):
        url_tmp = base_url + str(num)+'.html'
        getOnePage(url_tmp)
        print(num)



    endtime = time.time()
    print("Total use time: %.6f" % (endtime - starttime))
