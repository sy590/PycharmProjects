#数组形状
import numpy as np
#一维数组
t1 = np.arange(12)
print(t1)
print(t1.shape)

#二维数组
t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)

#三维数组
t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3)
print(t3.shape)

#修改数组形状
t4 = np.array(range(12))
print(t4.reshape((3,4)))

# 三维reshape
t5 = np.arange(24).reshape((2,3,4))
print(t5)

# 三维reshape成二维
t6 = t5.reshape((4,6))
print(t6)

# 三维reshape成一维
t7 = t5.reshape((24,))
print(t7)

# 三维reshape成二维
t8 = t5.reshape((24,1))
print(t8)

t9 = t5.reshape((1,24))
print(t9)

# 把多维数组按照行展开
t10 = t5.flatten()
print(t10)