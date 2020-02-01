#!/usr/local/bin/python3
import requests
from bs4 import BeautifulSoup
from urllib import request
import time
import os

# 爬取每日必应壁纸（国际版）
'''
必应国内版和国际版的区别是国内的时间比美国时间快13h，所以国内版的当日壁纸比国际版的图片要早出来。
国际版的页面上提供下载地址，且有水印。
'''

# 给出具体网址，并用requests进行网页爬取 国际版的下载按钮是进入网站后滚轮下滑出现的，不是静态页面，是通过js生成的动态页面。
url = 'https://cn.bing.com/hpm?FORM=BEHPTB&ensearch=1&IG=BD5D76C020BB4FE98F33E01CF1F3CF28&IID=SERP.1001&chunk=1'
webdata = requests.get(url).text

# 用BeautifulSoup对网页进行解析
soup = BeautifulSoup(webdata,'lxml')

# 找出图片所在的标签
img_address = soup.find('a',id='vs_bs_download')
a = 'https://cn.bing.com/'

# 图片的具体地址
link = a + img_address.get('href')
#print(link)

# 获取当前时间 格式为 ‘2019-11-21’
date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print ('D:/bing/BingWallpaper-' + date + '.jpg')

# 创建文件夹函数
def mkdir(path):
    folder = os.path.exists(path)

    if not folder: #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)
        print(path + " 文件夹创建成功！")
    else:
        return 0
        #print(path + " 文件夹已经存在.")
# 创建文件夹，将爬取的gif下载到所创建的文件夹中
file = "/home/liudao/BingWallpaper/bing-global" + "_" + date[0:7]
mkdir(file)


try:
    # 使用urllib库的urlretrieve()方法下载
    request.urlretrieve(link,file + '/BingWallpaper-global-' + date + '.jpg') # 图片文件示例名----BingWallpaper-2019-11-21.jpg
except Exception:
    # 国际版有时会遇到网页上声明不能下载，只好下载无水印版的。
    img_address = soup.select("#vert_iotd > div > div > div.vs_rowitem.vs_iotd_img > a > img")

    for i in img_address:
        link = i.get("src")
        links = a + link[0:-11] + "1920x1080.jpg"
    request.urlretrieve(links, file + '/BingWallpaper-global-' + date + '.jpg')

print(datetime + " 图片下载成功！")
