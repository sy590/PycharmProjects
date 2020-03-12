import numpy as np

us_file_path = "Data/US_video_data_numbers.csv"
uk_file_path = "Data/GB_video_data_numbers.csv"

t1 = np.loadtxt(us_file_path, delimiter=",",dtype="int",unpack=False)
# unpack 就是转置数据
t2 = np.loadtxt(us_file_path, delimiter=",",dtype="int",unpack=False)
#print(t1)
#print('*'*100)


# 其他转置方法
# print(t1.T)
# print('*'*100)
# print(t2.transpose())
# print('*'*100)
# print(t2.swapaxes(1,0))
print(t2)
print('*'*100)
# 取行，这里的2是第三行了，实际的第二行取1
print(t2[2])
print('*'*100)

# 取连续的多行
print(t2[2:])
print('*'*100)

# 取不连续的多行
print(t2[[2,8,10]])
print('*'*100)

# 取列 [,] 前面的是行，后面的是列          : 表示每个都要
print(t2[:,1])
print('*'*100)
print(t2[:,2:])
print('*'*100)
print(t2[:,[0,2]])
print('*'*100)
#取多行多列 取第三行，第四列的值
print(t2[2,3])
print('*'*100)

#取多行多列 取第三行到第五行，第二列到第四列
#取的是行和列交叉点的位置
b = t2[2:5,1:4]
print(b)
print('*'*100)

#取多个不相邻的点, 两个0 组合表示一个值，2，1组合表示另外一个值,第一个方括号标志点的横坐标，第二方括号表示点的纵坐标，选出来的结果是（0，0）,(2,1),(1,2)
c = t2[[0,2,1],[0,1,2]]
print(c)

# numpy 数值修改 直接取值，然后= 想要的值
