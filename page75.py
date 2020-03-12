import numpy as np

t1=np.arange(24).reshape(4,6)
print(t1)
print('*'*100)

#替换数值
print(t1<20)
t1[t1<20]=0
print(t1)
print('*'*100)
#替换数值by列
t1[:,0]=1
print(t1)
print('*'*100)

#条件替换
t2=np.where(t1<=1,100,300)
print(t2)
print('*'*100)

#numpy中的clib剪裁操作
t3=np.arange(30).reshape(5,6)
print(np.where(t3<10,5,100))
print('*'*100)

#处理N/A问题
t3=t3.astype(float)
t3[3,3]=np.nan
print(t3)
print('*'*100)

#将N/A转换成数值
t3[3,3]=0
print(t3)