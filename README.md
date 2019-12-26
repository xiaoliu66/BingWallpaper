# BingWallpaper
用python+termux+auto.js 在安卓平板上实现每日定时爬取必应壁纸
## 简介
利用Python写好的爬虫脚本，主要功能是抓取[必应](https://cn.bing.com)上的每日图片。因为身边并没有服务器，再说跑一个爬虫脚本也没必要去购买一个服务器来专门做爬虫。windows的笔记本也不可能每天都开着。所以想到了能不能利用自己身边其他的电子设备来帮助自己完成这个每天爬取图片的任务。   
经过上网查询后了解到可以使用安卓设备安装一个[termux](https://termux.com/)的软件来完成任务。下面是termux软件的有关介绍。

>Termux是一个Android下一个高级的终端模拟器, 开源且不需要root, 支持apt管理软件包，十分方便安装软件包, 完美支持Python, PHP, Ruby, Go, Nodejs, MySQL等。随着智能设备的普及和性能的不断提升，如今的手机、平板等的硬件标准已达到了初级桌面计算机的硬件标准, 用心去打造完全可以把手机变成一个强大的工具.    

简单来说安卓系统(本身就是基于Linux系统)的设备安装了termux的软件后，就可以在termux中用命令操作linux。和真正的linux系统还是有差别的。这个软件是不需要安卓设备拥有root权限的。

* [Termux下载地址](https://www.coolapk.com/apk/com.termux)    

Termux可以运行数据库、部署博客等等还有其他的用处,具体的详细情况见下：   
* [Termux 高级终端安装使用配置教程](https://www.sqlsec.com/2018/05/termux.html)   

>Auto.js 是一个不需要Root权限的JavaScript自动化软件。 

Auto.js 是可以在安卓系统上运行JS脚本的软件。这个软件可以做每天早上定时收取支付宝蚂蚁能量、各种app的签到、手机游戏脚本等等能做的事情很多。这个app之前是免费试用的，现在酷安只能找到Auto.js.pro 版本，需要注册并支付一定数额的金钱。下面会给出之前免费版本的下载地址。

* [Auto.js官方网站](https://hyb1996.github.io/AutoJs-Docs/#/)
* [Auto.js下载](https://github.com/Ericwyn/Auto.js/releases)      

## 操作步骤

1. 首先在安卓设备上安装好termux。在上面的 [Termux 高级终端安装使用配置教程](https://www.sqlsec.com/2018/05/termux.html) 中完成阅读"快速上手"到"访问外置存储优化",并且在termux中安装好python3和git。

2. 直接在termux中输入
> git clone git@github.com:xiaoliu66/BingWallpaper.git

其中bing-china.py和bing-global.py 就是必应的国内版和国际版的爬虫。在termux中输入
> crontab -e #添加定时脚本任务
> crontab -l #查看当前的定时脚本任务     

比如：自己的定时任务如下：
> 00 16 * * * python /你的python脚本所在的目录/bing-china.py >> /data/data/bing-china.log # 意思是每天的下午16点会定时执行这个爬取必应国内版的脚本并把信息添加到一个日志文件中。    

3.上面的定时任务需要在termux中启动crond服务，命令如下：
> crond start # crontab 服务启动
> crond stop # crontab 服务停止
> crond restart # crontab 服务重启

这个命令需要开启termux中自动输入，但是我在网上找资料是需要在Google play中下载一个Termux:boot 软件（需要付费且几年无更新过、Android 8中不能安装）。所以，我选择了在Auto.js中写了一个js脚本在启动termux后，自动输入crond start 启动crontab服务。 