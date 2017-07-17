from mayavi import mlab
import numpy as np

# 场景初始化
figure = mlab.gcf()
figure.scene.disable_render = True #所有物体全部建立完再绘制！


# 用mlab.points3d建立红色和白色小球的集合
x1, y1, z1 = np.random.random((3,10))
red_glyphs = mlab.points3d(x1, y1, z1, color=(1, 0, 0),resolution=10)
x2, y2, z2 = np.random.random((3, 10))
white_glyphs = mlab.points3d(x2, y2, z2, color=(0.9, 0.9, 0.9),resolution=10)
# 绘制选取框，并放在第一个小球上
outline = mlab.outline(line_width=3)
outline.outline_mode = 'cornered'
outline.bounds = (x1[0] - 0.1, x1[0] + 0.1,y1[0] - 0.1, y1[0] + 0.1,z1[0] - 0.1, z1[0] + 0.1)

# 处理选取事件
glyph_points =red_glyphs.glyph.glyph_source.glyph_source.output.points.to_array()

figure.scene.disable_render = False
def picker_callback(picker):
    if picker.actor in red_glyphs.actor.actors:
        # 计算哪个小球被选取
        point_id = int(picker.point_id / glyph_points.shape[0])  # int向下取整        
        if point_id != -1:#如果没有小球被选取，则point_id = -1
            # 找到与此红色小球相关的坐标
            x, y, z = x1[point_id], y1[point_id], z1[point_id]
            # 将外框移到小球上
            outline.bounds = (x - 0.1, x + 0.1,
                              y - 0.1, y + 0.1,
                              z - 0.1, z + 0.1)
    if picker.actor in red_glyphs.actor.actors:
        # 计算被选取的小球的ID号
        point_id = int(picker.point_id / glyph_points.shape[0])
        if point_id != -1:
        # 计算与此红色小球相关的坐标
            x, y, z = x1[point_id], y1[point_id], z1[point_id]
            # 将外框移到小球上
            outline.bounds = (x - 0.1, x + 0.1,y - 0.1, y + 0.1,z - 0.1, z + 0.1)  


picker = figure.on_mouse_pick(picker_callback)  
picker.tolerance =  0.01   #设置tolerance参数，提高选取精度！
mlab.title('Click on red balls')#设置窗口的标题文字
mlab.show() 