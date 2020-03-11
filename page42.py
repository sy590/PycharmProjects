from matplotlib import pyplot as plt
import matplotlib

font = {"family": 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 7}
matplotlib.rc("font", **font)
matplotlib.rc("font", family='MicroSoft YaHei', weight="bold")

x = ["猩球崛起3：\n终极之战","敦刻尔克","蜘蛛侠：\n英雄归来","战狼2"]
y_16 = [15746,312,4497,319]
y_15 = [12357,156,2045,168]
y_14 = [2358,399,2358,362]

bar_width=0.3
x_14 = list(range(len(x)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]
plt.bar(x_14,y_14,width=bar_width,label='9月14日')
plt.bar(x_15,y_15,width=bar_width,label='9月15日')
plt.bar(x_16,y_16,width=bar_width,label='9月16日')

# 对应标签
xtick_labels = {format(i) for i in x}
plt.xticks(x_15,xtick_labels)
plt.xlabel('电影名称')
plt.ylabel('票房金额（亿）')
plt.title('9月14日-9月16日票房情况汇总')
plt.grid(alpha=0.3)
plt.legend()
plt.show()