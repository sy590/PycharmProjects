from matplotlib import pyplot as plt
import matplotlib
font = {"family": 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 7}
matplotlib.rc("font", **font)
matplotlib.rc("font", family='MicroSoft YaHei', weight="bold")

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(quantity)),quantity,width=1)

x=[i-0.5 for i in range(12)]
xtick_labels=interval
plt.xticks(x,xtick_labels)
plt.grid()
plt.show()