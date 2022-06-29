# -*- coding:utf-8 -*-
# @Time   : 2021-08-03
# @Author : carl_DJ

"""如果引用的库未安装，则自动安装""" 
#为了明确异常信息，我们追加断言
try:
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    import jieba
    import jieba.analyse
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud,STOPWORDS
    import numpy as np
    from PIL import Image
# 使用pip.main()方法进行依赖库的安装（例举几个常用的库）   
except  ImportError:
    import pip
    pip.main(["install", "--user", "requests","beautifulsoup4","matplotlib","wordcloud","pandas","pillow"])
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    import jieba
    import jieba.analyse
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud,STOPWORDS
    import numpy as np    
    from PIL import Image 