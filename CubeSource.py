from tvtk.api import tvtk
#创建一个长方体数据源，并且同时设置其长宽高
s = tvtk.CubeSource(x_length=1.0,y_length=2.0,z_length=3.0)
#使用PolyDataMapepr将数据转化为图形数据
m = tvtk.PolyDataMapper(input_connection=s.output_port)
#以上为可视化管线
#================
#以下为图行管线
#创建一个Actor
a = tvtk.Actor(mapper=m)
#创建一个Renderer,并对图像背景设置一种颜色，将Actor添加进去。
r = tvtk.Renderer(background=(0,0,0))
r.add_actor(a)
#创建一个RenderWindow(窗口)，将Renderer添加进去
w = tvtk.RenderWindow(size=(350,350))
w.add_renderer(r)
#创建一个RenderWindowInteractor(窗口交互工具)
i = tvtk.RenderWindowInteractor(render_window=w)
#================
#开启交互
i.initialize()
i.start()