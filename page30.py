from matplotlib import pyplot as plt
import matplotlib

font = {"family": 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 7}
matplotlib.rc("font", **font)
matplotlib.rc("font", family='MicroSoft YaHei', weight="bold")

y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 4, 4, 2, 3, 3, 4, 1, 2, 1, 1, 1, 1, 1, 1, 1]
y_3 = [0, 0, 1, 1, 2, 4, 7, 2, 3, 3, 4, 1, 2, 1, 1, 0, 1, 0, 1, 0]
x = range(11, 31)

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 设置X轴刻度
_xtick_labels = ["{}.岁".format(i) for i in x]

plt.xticks(x, _xtick_labels)
plt.yticks(range(0, 7))



# 绘制网格
plt.grid(alpha=0.4,linestyle=":")


# 展示&16进制颜色 https://www.sioe.cn/yingyong/yanse-rgb-16/
plt.xlabel("年龄")
plt.ylabel("女朋友个数")
plt.title("10-31岁交女朋友个数统计")
plt.plot(x, y_1, label="自己", color="Crimson",linestyle="--", linewidth=5)
plt.plot(x, y_2, label="同桌1", color="Magenta",linestyle=":")
plt.plot(x, y_3, label="同桌2", color="PaleVioletRed",linestyle="-.")

# 添加图列
plt.legend()

plt.show()
