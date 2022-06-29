# -*- coding:utf-8 -*-
# @Time   : 2021-08-03
# @Author : carl_DJ

import os

#需要安装的库
libs = ["requests","beautifulsoup4","matplotlib","wordcloud","pandas","pillow"]

#循环遍历安装
for lib in libs:
    os.system("pip install " + lib)