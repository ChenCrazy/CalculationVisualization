#使用ivtk显示立方体的程序
from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI 
#为了使用ivtk导入与其相关的几个库
#图形管线
s = tvtk.CubeSource(x_length=1.0,y_length=2.0,z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)

#创建一个带Crust(Python Shell)窗口的GUI对象
gui = GUI()
#构建窗口
win = ivtk.IVTKWithCrustAndBrowser()
#构建整个IVTK工具
win.open()
win.scene.add_actor(a)

#修正子窗口脱离主窗口问题
dialog = win.control.centralWidget().widget(0).widget(0)
from pyface.qt import QtCore
dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
dialog.show()

#开始界面消息循环
gui.start_event_loop()
