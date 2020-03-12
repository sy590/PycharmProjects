import numpy as np
t10 = np.arange(18)
t11 = np.arange(27)
t12 = t10.reshape((3,3,2))
t13 = t11.reshape((3,3,3))

t14 = np.arange(6)
t15 = t14.reshape((3,2))
t16 = np.arange(9)
t17 = t16.reshape((3,3))

# 3,3,2 + 3,2
print(t12+t15)

# 3,3,3+ 3,2 就不行 数组要进行计算，那么需要至少有一个维度需要相等，或者有一方的维度等于1.（3,2,1) (,,1） 或者（3，2，1）和（,2,1)
