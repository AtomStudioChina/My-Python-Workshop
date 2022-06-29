import os,sys
from time import *
while True:
	search=input("检索第三方库：")
	os.system("pip install " + search) # 选择其中一个镜像源，下载安装库。