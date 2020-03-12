import numpy as np

t1 = np.arange(12).reshape(2, 6)

t2 = np.arange(12, 24).reshape(2, 6)

print(t1)
print(t2)
print('*' * 100)

#竖直拼接
t3 = np.vstack((t1, t2))
print(t3)
print('*' * 100)
#水平拼接
t4 = np.hstack((t1,t2))
print(t4)
print('*' * 100)

# 行交换 1,2 表示选中第二行和第三行，2,1 表示选中第三行和第二行
t3[[1,2],:] = t3[[2,1],:]

print(t3)
print('*' * 100)


# 列交换
t3[:,[0,2]] = t3[:,[2,0]]
print(t3)
print('*' * 100)
