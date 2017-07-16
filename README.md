<span id = "readme"></span>

〇、Python科学计算三维可视化
========
## 科学计算可视化
* 信息可视化
    非空间的非数值的高维信息进行可视化：信息 知识

* 科学可视化
    空间技术可视化
## 科学计算可视化的主要方法
* 二维标量数据场
    1. 颜色映射法：将颜色和数据之间映射关系
    2. 等值线方法：F（xi,yi）=f（f为给定的值）一组数值表示连续面状的图像，使其数值特征渐变的一种方法
    3. 立体图法和层次分割法：结合使用，用在地形数据场可视化处理。立体图法，用立体图形显示平面数据，将平面数据场的数据转换为高度。层次分割法，把立体图像法进一步扩展，并对立体图中的三角面片进行分层，使得各层之间具有明确的层次分割线
* 三维标量数据场
    1. 面绘制方法：用图形的手段还原出图形的三维空间结构，并以表面的形式表现出来
    2. 体绘制方法：不仅仅展示表面的细节，更是体内部的细节。体绘制将三维空间体内部的细节直接转换至最后的立体图像，中间过程中不需要中间几何图元
* 矢量数据场
    1. 直接法：矢量数据本身即具有方向又具有大小，因此在可视化过程中，可以用箭头、线段、色轮等手段表示矢量数据
    2. 流线法：体现了流场空间个点在同一瞬间的流动概念，流场上每一点的切线可以表示该点流体的流动方向、大小，由流线的密度给出。
## 应用领域
 地球科学、大气科学、医学生命、生物/分子科学、航空/航天/工业、化工/化学、物理/力学、人类考古/地质勘探等。  

---
---

# 壹、三维可视之基础运用
## 1.TVTK库入门
Python第三方库TVTK，讲解科学计算三维表达和可视化的基本概念。
### [TVTK中所有库的细节](http://code.enthought.com/projects/)

### 基础库
依次安装：  
VTK-7.1.1-cp36-cp36m-win_amd64.whl  
numpy-1.12.1+mkl-cp36-cp36m-win_amd64.whl   
traits-4.6.0-cp36-cp36m-win_amd64.whl   
mayavi-4.5.0+vtk71-cp36-cp36m-win_amd64.whl   
PyQt4-4.11.4-cp36-cp36m-win_amd64.whl   
[相关库下载](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

### TVTK文档查看细节描述
        >>> from tvtk.tools import tvtk_doc   
        >>> tvtk_doc.main()
       
### TVTK帮助资源
* [VTK所有方法](http://www.vtk.org/doc/nightly/html/annotated.html)  
* TVTK的类名去除了前缀vtk
* 函数名按照python的惯例，采用下划线连接单词
    `如：AddItem -> add_item`  
* VTK对象的方法在TVTK中用Trait属性代替  
    ```Python
    如m.SetInputConnection(c.GetOutputPort())    //VTK  
    ——>  m.input_connection(c.output_port)         //TVTK 
    ```


### Tvtk库的基本三维对象
---------
|三维对象|说明|
|-------|----|
|CubeSource|立方体三维数据对象源|
|ConeSource|圆锥三维数据对象源|
|CyllinerSource|圆柱三维数据对象源|
|ArcSource|圆弧三维对象数据源|
|ArrowSource|箭头三维对象数据源|


### CubeSource对象的属性
---------
|属性|说明|
|-----------|------------------------------|
| s.x_length|长方体对象在X轴方向的长度|
| s.y_length|长方体对象在y轴方向的长度|
| s.z_length|长方体对象在z轴方向的长度|
| s.center|长方体对象所在坐标的原点:|
| s.output_points_precission|长方体对象的精度:|


### CubeSource对象的方法
----------
|VTK方法    |  Tvtk|说明|
|------------|------|-----|
|Set/GetXLength()|x_length|设置/获取长方体对象在X轴方向的长度|
|Set/GetCenter()|center|设置/获取长方体对象所在坐标系的原点|
|...|...|...|


## 2.TVTK管线与数据加载  
### 管线技术（Pipline,流水线技术）
![理解TVTK的管线](https://github.com/CrazyChen/CalculationVisualization/raw/master/img/理解Tvtk的管线.png)  
将各个对象串连起来，每个对象只需要实现相对简单的功能，整个管线根据需求实现复杂的数据可视化处理，每个对象随着用户的交互不断的发生更新。
* 可视化管线  
将原始数据加工成图形数据的过程  
* 可视化管线相关的对象  
-----------
| TVTK对象 | 说明 |
|----|----|
|CubeSource|通过程序内部计算输出一组描述长方体的数据（PolyData）|
|PolyDataMapper|PolyData通过该映射器将数据映射为图形数据(mapper)|

* 图形管线  
图形数据加工为我们提供看到的图像的过程  
-----------  
| TVTK对象 | 说明 |
|----|----|
|Actor|场景中的一个实体。它包括一个图形数据（mapper），具有描述该实体的位置、方向、大小的属性。|
|Renderer|渲染的场景。它包括多个需要渲染的Actor。|
|RenderWindow|渲染用的图形窗口，它包括一个或者多个Render。|
|RenderWindowInterActor|给图形窗口提供一些用户交互功能，交互操作并不改变Actor或者图形数据的属性，只是调整场景中的Camera的一些设置|

### IVTK工具观察TVTK管线
为了方便操作和观察各个TVTK的管线，可以交互式的修改各个TVTK对象的属性，TVTK库提供了一个IVTK工具。使用该工具，可以使用鼠标点击相应窗口上的按钮来查看各个TVTK库的对象属性。
使用`from tvtk.api import ivtk`引入该工具。
### TVTK数据集(Dataset)
#### 相关概念
* 点(Point)和数据(Data)
* 点之间:连接 VS 非连接
* 多个相关的点组成单元(cell)
* 点的连接: 显式 VS 隐式
* 数据:标量(Scalar) VS 矢量(Vector) 
    数据既可以属于点也可以属于单元
#### 五种数据集
-----
|VTK name|Connectivy（点连接关系）|Suitable for|Required information|介绍特点|  
|:---|:---|:---|---|------|  
|ImageData|Implicit（隐性）|Volumes and surfaces| (apacing(三维网格数据的起点坐标),origin(三维网格数据在XYZ轴上的间距),dimensions(在XYZ轴上的网格数))|表示二维或三维图像的数据结构，可描述为二维或三维数组。在数组中存放数据，点位于正交且等距的网格上，不需要给出坐标，点之间的连接关系由各自在数组中的位置确定|  
|RectilinearGrind|Implicit|Volumes and surfaces| get_point(n)|间距不均匀的网格，所有的点都在正交的网格上。因为间距不均匀，需要给出X、Y、Z各个网格在平面的位置。[示例](Example_RectilinearGrid.py)|  
|StructuredGrid|Implicit|Volumes and surfaces| get_cell(n)|创建任意形状的网格，需要给出点的坐标。需要point、dimensions和polydata|  
|PolyData|Explicit|Point,lines and surfaces|points，verts，line ，polys |描述一组三维空间中的点、线、面的数据结构：由一系列的点、点之间的联系以及由点构成的多边形组成。这些信息需要用户设置，因此程序创建时很繁琐，TVTK中的很多三维模型都能输出PolyData对象|
|UnstructuredGrid|Explicit|Volumes and surfaces| ...|......|  

### TVTK库的数据加载
大多数可视化应用的数据，并非都是TVTK库构建，更多的是通过外部接口读取外部数据文件。VTK的建模功能并不强大，因此它支持许多种格式的文件，能将其它软件产生的数据通过各种Reader类读入VTK，放到流水线上处理。[TVTK扩展阅读](http://old.sebug.net/paper/books/scipydoc/tvtk_intro.html)  
  
## 3.TVTK库可视化实例   
本部分展示三个示例：[标量可视化](PLOT3Dcontours.py)、[矢量可视化](PLOT3Darrow.py)、[轮廓线可视化](PLOT3Doutline.py)。  
-----
  
[回到顶部](#readme)  

-----
----- 

# 贰、三维可视之高级进阶  

## 1、Mayavi库介绍和入门基础  
Mayavi中主要有两大部分功能：一类是处理图形可视化和图形操作mlab模块，一类是创建管线对象、窗口对象的API。
### Mayavi基本元素 
* Mayavi.mlab  

|类 别|内容|说明|  
|---|---|---|
|绘图函数|barchar、contour3d、contour\_surf、flow、imshow、mesh、plot3d、points3d、quiver3d、surf、triangular_mesh|对已有的数据实现可视化显示，数据可以是numpy构建的，也可以是从外部数据读取的。既可以对一个曲面可视化，也可以对一个经过三维扫描后得到的数据进行三维可视化。|
|图形控制函数|clf、close、draw、figure、gcf、savefig、screenshot、sync\_camera|对Mayavi中的figer进行控制。比如可以通过gcf来获取当前对象的指针，也可以通过clf来清空当前的图形。|
|图形修饰函数|colorbar、scalarbar、xlabel、ylabel、zlabel|对当前的图形进行一定是修饰和装饰，比如说绘制完一个图形后需要增加一个颜色标识栏，或者对坐标轴增加相应的标签等。|
|相机控制函数|move、pitch、roll、view、yaw|对相机进行操作。移动旋转等。|
|其他函数|animate、axes、get\_engine、show、set\_engine……|animate生成一段动态的可视化效果、get\_engine获得当前管线的engine等。|
|Mlab管线控制|Open、set\_vtk\_src、adddataset、scalar\_cut\_plane|设置当前VTK的管线数据源。也可以对当前的绘制管线增加数据集adddataset|  

---
* Mayavi API  

|类 别|内容|说明|
|---|---|---|
|管线基础对象|Scene、Source、Filter、ModuleManager、Module、PipelineBase、Engine|通过这类函数获得当前mayavi管线中的各个基本对象|
|主视窗和UI对象|DecoratedScene、MayaviScene、SceneEditor、MlabSceneModel、EngineView、EngineRichView|通过这类函数实现在其他库中构建的用户界面里嵌入mayavi窗口。比如mayavi结合TraitsUI构建一个可交互的三维可视化应用。|
---  
### 快速绘图实例  
[快速绘制实例1]("MayaviDemo1.py")  
![]("img\mayavidemo1.png")  

[快速绘制实例2]("MayaviDemo2.py")  
![]("img\mayavidemo2.png")  
 
### Mayavi管线
#### Mayavi管线的层级  
* Engine：建立和销毁Scenes  
* Scenes：多个数据集合Sources  
* Filters：对数据进行变换  
* Module Manager：控制颜色，Colors and Legends  
* Modules：最终数据的表示，如线条、平面等  
* 除使用视图外，mlab.show_pipeline()也能打开mayavi管线的对话框
#### 管线中的对象
* Mayavi Scene:处于树的最顶层的对象，表示场景。
* GridSource: 网格数据源,在配置界面中，每一项为每个点标量数据的名称。
* PlolyDataNormals :数据源的法向量
### 程序配置属性的步骤
1、获得场景对象，mlab.gcf()  
2、通过children属性，在管线中找到需要修改的对象  
3、配置窗口有多个选项卡，属性需要一级一级获得  
  
---

## 2、Mlab基础  
mlab提供的面向脚本API，实现快速的三维可视化。mayavi通过绘图函数对numpy数组建立可视化。
### mlab对Numpy建立可视化过程：
1.建立数据源
2.使用Filter对数据进行加工(可选)
3.添加可视化模块
###





**Mayavi可视化实例**~~

[回到顶部](#readme)
~~# 叁、三维可视之交互界面  
**Traits基础**  
**TraitUI库的基本使用和交互式三维可视化应用开发**  
**TraitUI与Mayavi结合实例**  
Python第三方库Mayavi，讲解科学计算三维表达和可视化的使用方法。  
Python第三方库TraitUI，讲解交互式科学计算三维效果应用的开发方法。~~
[回到顶部](#readme)
~~# 四、三维可视之运算  
**SciPy库的介绍和拟合与统计运算**  
**SciPy库的线性代数、积分和差值等运算**  
**SciPy库实例**~~  
