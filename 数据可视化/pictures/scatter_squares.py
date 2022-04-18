import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolor='none', s=40)

#标题
plt.title("Square Numbers", fontsize=24)

#标签
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#刻度大小
plt.tick_params(axis='both', which='major', labelsize=14)

#坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])

#显示
plt.show()
