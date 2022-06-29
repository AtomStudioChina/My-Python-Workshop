# 导入需要的包
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 以下三行是为了让matplot能显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(8, 8))
# 注意几个新增的参数, width和height是用来控制放大尺度的
# 分别代表投影的宽度和高度(8E6代表 8x10^6米)
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6,
            lat_0=23, lon_0=113,)
m.bluemarble(scale=0.5)

# 这里的经纬度是：(经度, 纬度)
x, y = m(113, 23)
plt.plot(x, y, 'ok', markersize=5) 
plt.text(x, y, '深圳', fontsize=12, color="red") 
plt.show()
plt.savefig('2D深圳.png')