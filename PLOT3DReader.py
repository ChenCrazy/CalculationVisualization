from tvtk.api import tvtk


def read_data():  #读入数据
    plot3d = tvtk.MultiBlockPLOT3DReader( 
        xyz_file_name=" Element\combxyz.bin ",#网格文件
        q_file_name=" Element\combq.bin ",#空气动力学结果文件
        scalar_function_number=100,  #设置标量数据数量
        vector_function_number=200  #设置矢量数据数量
        )
    plot3d.update()
    return plot3d

####


plot3d = read_data()
grid = plot3d.output.get_block(0)
