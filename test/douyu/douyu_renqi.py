# coding:utf-8
import requests
import time
import gevent
import random
from bs4 import BeautifulSoup
from lxml import etree

from multiprocessing.dummy import Pool as threadspool
import urllib,re,time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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



url = "http://www.douyu.com/g_jdqscjzc"



def getOnePage(page_url):
    req = requests.get(page_url,headers=headers, proxies=random.choice(IPs))
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'html.parser')

    room_num = soup.find_all(attrs={"class":"play-list-link"})
    room_name = soup.find_all(attrs={"class":"dy-name ellipsis fl"})
    room_people = soup.find_all(attrs={"class":"dy-num fr"})

    # 创建空列表
    room_list = []
    #print(room_name[0].text + ':'+room_people[0].text+'\n')
    #print('直播数量: \n')
    if(len(room_name) == len(room_people)):
        for i in range(len(room_name)):
            dict_room={'room_num':room_num[i].text,
                        'room_name':room_name[i].text,
                        'room_people':room_people[i].text[:-2]}

            room_list.append(dict_room)


    print(room_list)

    return room_list


if __name__ == '__main__':
    getOnePage(url)




