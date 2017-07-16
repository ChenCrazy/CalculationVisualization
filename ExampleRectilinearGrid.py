from tvtk.api import tvtk
import numpy as np
#网格构建Rectilinear
#因为Rectilinear中网格构建不均匀，所以需要设置X/Y/Z各个网格在平面的位置
x = np.array([0,3,9,15])
y = np.array([0,1,5])
z = np.array([0,2,3])
#上面所有点的交点构建成Rectilinear网格上对象上的所有点
r = tvtk.RectilinearGrid()

r.x_coordinates = x
r.y_coordinates = y
r.z_coordinates = z
# 因为它的对象不会根据三个数组的长度自动调整dimensions的属性
#将numpy三个数组求得各自长度赋值给数据对象的dimesions属性
r.dimensions = len(x),len(y),len(z)

#通过输出查看数据集中的细节（循环语句）
#for n in range(6):
#   print(r.get_point(n))
