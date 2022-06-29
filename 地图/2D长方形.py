# 导入需要的包
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from itertools import chain

# 以下三行是为了让matplot能显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False

def draw_point(m, x, y, name):
    # 这里的经纬度是：(经度, 纬度)
    x, y = m(x, y)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, name, fontsize=12, color="red")

def draw_map(m, scale=0.2):
    # 绘制带阴影的浮雕图像
    m.shadedrelief(scale=scale)

    # 根据经纬度切割，每13度一条线
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # 集合所有线条
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)

    # 循环画线
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')

fig = plt.figure(figsize=(8, 6), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180,)
locations = {
    '泰姬陵': (17, 78),
    '吉萨金字塔群': (29, 31),
    '英国的巨石阵': (51, 1),
    '巴黎圣母院': (48, 2),
    '卢浮宫': (48, 2),
    '红场和克里姆林': (55, 37),
    # ...
}
draw_map(m)
for loc in locations:
    print(locations[loc])
    draw_point(m, locations[loc][1], locations[loc][0], loc)
plt.show()
plt.savefig('2D长方形.png')