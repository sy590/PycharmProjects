import numpy as np

t4=np.arange(24)
t5=t4.reshape(4,6)
print(t5)

t1= np.array([0,1,2,3,4,5,6,7,8,9,10,0,1,2,3,4,5,6,7,8,9,10,0,1])
t2= t1.reshape(4,6)

print(t2)

print(t5+t2)

t3 = np.array([0,1,2,3,4,5])
print(t5)
print(t3)
print(t5+t3)

t6=np.arange(100,124).reshape(4,6)
print(t6)
print(t6-t5)

t4=np.arange(4)
t8= t4.reshape(4,1)
print(t8)
print(t6-t8)

t9 = np.arange(10)
print(t9)


