'''使用ivtk显示立方体的程序'''
def ivtk_scene(actors):
    from tvtk.tools import ivtk
    #创建一个带Crust(Python Shell)窗口的GUI对象
    win = ivtk.IVTKWithCrustAndBrowser()
    #构建整个IVTK工具
    win.open()
    win.scene.add_actor(actors)
    #修正子窗口脱离主窗口问题
    dialog = win.control.centralWidget().widget(0).widget(0)
    from pyface.qt import QtCore
    dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
    dialog.show()
    return win

def event_loop():
    from pyface.api import GUI
    gui = GUI()
    #开始界面消息循环
    gui.start_event_loop()
#以上部分可封装成独立的模块，待创建对象时调入使用
#========================
'''from tvtk.api import tvtk
#图形管线
s = tvtk.CubeSource(x_length=1.0,y_length=2.0,z_length=3.0)
m = tvtk.PolyDataMapper(input_connection=s.output_port)
a = tvtk.Actor(mapper=m)
win = ivtk_scene(a)
win.scene.isometric_view()
event_loop()'''