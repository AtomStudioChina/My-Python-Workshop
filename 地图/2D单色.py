from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
map = Basemap()
map.drawcoastlines()
plt.show()
plt.savefig('2D单色.png')