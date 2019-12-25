import requests
from bs4 import BeautifulSoup
from urllib import request
import time
import os
# 爬取每日必应壁纸（国内版）
'''
必应国内版和国际版的区别是国内的时间比美国时间快13h，所以国内版的当日壁纸比国际版的图片要早出来。
国际版的页面上提供下载地址，且有水印。
'''

# 给出具体网址，并用requests进行网页爬取
url = 'https://cn.bing.com/'
webdata = requests.get(url).text

# 用BeautifulSoup对网页进行解析
soup = BeautifulSoup(webdata,'lxml')

# 找出图片所在的标签
img_address = soup.find('div',id ='bgImgProgLoad')
a = 'https://cn.bing.com/'

# 图片的具体地址
# print(a + img_address.get('data-ultra-definition-src'))
link = a + img_address.get('data-ultra-definition-src')

# 获取当前时间 格式为 ‘2019-11-21’
date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
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
file = "D:\\bing"
mkdir(file)

# 使用urllib库的urlretrieve()方法下载
request.urlretrieve(link,file + '/BingWallpaper-' + date + '.jpg') # 图片文件示例名----BingWallpaper-2019-11-21.jpg
