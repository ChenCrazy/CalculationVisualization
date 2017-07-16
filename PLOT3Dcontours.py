from tvtk.api import tvtk
from CStvtkfunc import ivtk_scene, event_loop

plot3d = tvtk.MultiBlockPLOT3DReader(
    xyz_file_name="Element\combxyz.bin",
    q_file_name="Element\combq.bin",
    scalar_function_number=100, vector_function_number=200
)  # 读入Plot3D数据
plot3d.update()  # 让plot3D计算其输出数据
grid = plot3d.output.get_block(0)  # 获取读入的数据集对象

con = tvtk.ContourFilter()  # 等值面过滤器，创建等值面对象
con.set_input_data(grid)
con.generate_values(10, grid.point_data.scalars.range)  # 指定轮廓数和数据范围

# 设定映射器的变量范围属性
m = tvtk.PolyDataMapper(scalar_range=grid.point_data.scalars.range,
                        input_connection=con.output_port)
a = tvtk.Actor(mapper=m)
a.property.opacity = 0.5  # 设定透明度为0.5
# 窗口绘制
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()
