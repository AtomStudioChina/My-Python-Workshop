import os,sys
from time import *
while True:
	search=input("检索第三方库：")
	web = "https://pypi.tuna.tsinghua.edu.cn/simple "  # 清华大学镜像源。
	# web = "http://mirrors.aliyun.com/pypi/simple "  # 阿里云镜像源。
	# web = "https://pypi.mirrors.ustc.edu.cn/simple "  # 中国科技大学镜像源。
	# web = "http://pypi.douban.com/simple "  # 豆瓣镜像源。
	os.system("pip3 install -i "+ web + search) # 选择其中一个镜像源，下载安装库。