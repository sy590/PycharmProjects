from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# windows 和 Linux 设置字体的方法
font = {"family": 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 7}
matplotlib.rc("font", **font)
matplotlib.rc("font", family='MicroSoft YaHei', weight="bold")


# my_font = font_manager.FontPorperties(fname = "\AppData\Local\Microsoft\FontCache\4\CloudFonts\TTC")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)

# 调整X轴的刻度

_x = list(x)
_xtick_labels = ["10点,{}分".format(i) for i in range(60)]
_xtick_labels += ["11 点,{}分".format(i) for i in range(60)]
# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(_x[::3], _xtick_labels[::3], rotation=90)  # FontProperties=my_font) #ratation旋转的度数

# 添加legend
plt.xlabel("时间")
plt.ylabel('温度 单位（℃）')
plt.title("10点到12点每分钟的气温变化情况")

plt.show()
