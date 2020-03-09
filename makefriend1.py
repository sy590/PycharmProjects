from matplotlib import pyplot as plt
import matplotlib
font = {"family": 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 7}
matplotlib.rc("font", **font)
matplotlib.rc("font", family='MicroSoft YaHei', weight="bold")

x = range(11, 30)
y = (0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1)

plt.figure(figsize=(20, 8), dpi=80)
plt.xlabel('Age')
plt.ylabel('个')
plt.title("age with girl friend")
plt.plot(x, y)
plt.show()
