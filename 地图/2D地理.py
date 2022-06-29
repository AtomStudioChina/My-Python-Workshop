# 导入需要的包
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 初始化图形
plt.figure(figsize=(8, 8))
# 底图：圆形, lat_0：纬度；lon_o: 经度, (113,29)是武汉
m = Basemap(projection='ortho', resolution=None, lat_0=29, lon_0=113)
# 底色
m.bluemarble(scale=0.5)
# 显示
plt.show()