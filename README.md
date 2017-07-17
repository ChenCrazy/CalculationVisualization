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

| TVTK对象 | 说明 |
|----|----|
|CubeSource|通过程序内部计算输出一组描述长方体的数据（PolyData）|
|PolyDataMapper|PolyData通过该映射器将数据映射为图形数据(mapper)|

* 图形管线  
图形数据加工为我们提供看到的图像的过程   
 
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


* Mayavi API  

|类 别|内容|说明|
|---|---|---|
|管线基础对象|Scene、Source、Filter、ModuleManager、Module、PipelineBase、Engine|通过这类函数获得当前mayavi管线中的各个基本对象|
|主视窗和UI对象|DecoratedScene、MayaviScene、SceneEditor、MlabSceneModel、EngineView、EngineRichView|通过这类函数实现在其他库中构建的用户界面里嵌入mayavi窗口。比如mayavi结合TraitsUI构建一个可交互的三维可视化应用。|
---
### 快速绘图实例  
[快速绘制实例1](MayaviDemo1.py)  
![](img\mayavidemo1.png)  

[快速绘制实例2](MayaviDemo2.py)  
![](img\mayavidemo2.png)  
 
--- 
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
>1、获得场景对象，mlab.gcf()  
>2、通过children属性，在管线中找到需要修改的对象  
>3、配置窗口有多个选项卡，属性需要一级一级获得  
   
[回到顶部](#readme)

---

## 2、Mlab基础  
mlab提供的面向脚本API，实现快速的三维可视化。mayavi通过绘图函数对numpy数组建立可视化。
### mlab对Numpy建立可视化过程：
>1.建立数据源  
>2.使用Filter对数据进行加工(可选)  
>3.添加可视化模块  

#### 3D绘图函数——0D和1D数据  
* Point3d（）:基于Numpy数组x、y、z提供的三维点坐标，绘制点图形
* Plot3d（）:基于1维Numpy数组x、y、z提供的三维坐标数据，绘制线图形

##### 1、3D绘图函数——points3d()  
函数调用形式：     
points3d(x, y, z,...)  
points3d(x, y, z, s, ...)   
points3d(x, y, z, f, ...)  
x,y,z表示numpy数组、列表或者其他形式的点三维坐标。s表示在该坐标点处的标量值。f表示通过函数f（x，y，z）返回的标量值   
  
|参数|说明|
|---|---|
|color |VTK对象的颜色，定义为(0,1)的三元组。如白色[1,1,1]|
|colormap|colormap的类型，例如Reds、Blues、Copper等|
|extent |x、y、z数组范围[xmin, xmax, ymin, ymax, zmin, zmax]|
|figure |画图|
|line_width |线的宽度，该值为float，默认为0.2|
|mask_points |减少/降低大规模点数据集的数量,可用于快速清晰的绘制|
|mode |显示符号的模式，例如2darrow、2dcircle、arrow、cone等|
|name |VTK对象名字|
|opcity |Vtk对象的整体透明度，该值为float型，默认为1.0|
|reset_zoom |对新加入场景数据的放缩进行重置。默认为True|
|resolution |符号的分辨率，如球体的细分数，该值为整型，默认为8|
|scale_factor |符号放缩的比例|
|scale_mode |符号的放缩模式，如vector、scalar、none|
|transparent| 根据标量值确定actor的透明度|
|vmax |对colormap放缩的最大值|
|vmin| 对colormap放缩的最小值|
>points3d(x, y, z, s, colormap="Reds", scale_factor=.25)   

**我们可以看到，point3d参数的描述是对VTK对象的一个整体描述。mayavi是对VTK对象的一个封装，因此mayavi建立的对象也就是VTK的对象**  
   
##### 2、3D绘图函数-plot3d ()   
函数调用形式：  
plot3d(x, y, z,...)  
plot3d(x, y, z, s, …)  
x,y,z表示numpy数组，或列表。给出了线上连续的点的位置,s表示在该坐标点处的标量值    
__参数:__color、colormap、extent、figure、line\_width、name、opacity、representation、reset\_zoom、transparent、**` tube_radius`、`tube_sides`**、vmax、vmin    
|参数| 说明|
|---|---|
|tube_radius |线管的半径，用于描述线的粗细|
|tube_sides |表示线的分段数，该值为整数，默认为6|
  
>plot3d(x, y, z, np.sin(mu), tube_radius=0.025,colormap=‘Spectral’)  
>x,y,z表示numpy数组，给出了线上连续的点的位置,np.sin(mu)表示在该坐标点处的标量值
>tube_radius绘制线的半径为0.025,colormap采用Spectral颜色模式。  
   
 [回到顶部](#readme)

---

#### 3D绘图函数-2D数据  
基于二维数组的Mlab3D绘图函数:  
* imshow() :将二维数组可视化为一张图像  
* surf() :将二维数组可视化为一个平面，Z轴描述了数组点的高度  
* contour_surf() :将二位数组可视化为等高线，高度值由数组点的值来确定   
* mesh() :绘制由三个二维数组x、y、z描述坐标点的网格平面   
* barchart() :根据二维、三维或者点云数据绘制的三维柱状图   
* triangular_mesh():绘制由x、y、z坐标点描述的三角网格面    
     
##### 3、3D绘图函数-imshow()   
函数调用形式: imshow(s,...)
__参数:__color、colormap、extent、figure、**`interpolate`**、line\_width、name、opacity、reset\_zoom、transparent、vmax、vmin      
|参数 |说明|
|---|---|
|interpolate |图像中的像素是否被插值，该值为布尔型，默认为True|
  
##### 4、3D绘图函数-surf()  
求解曲面。
函数调用形式:  
surf(s,...)  
surf(x,y,s,...)   
surf(x,y,f,...)  
s是一个高程矩阵，用二维数组表示。  

##### 5、3D绘图函数-contour_surf()  
求解等值线。与surf类似。  

#### 3D绘图函数-3D数据   
* contour3d():三维数组定义的体数据的等值面可视化。  
* quiver3d(): 三维矢量数据的可视化，箭头表示在该点的矢量数据。  
* flow() :绘制三维数组描述的向量场的粒子轨迹。  
    
##### 5、3D绘图函数-contour3d()  
函数调用形式：  
contour3d(scalars, …)  
contour3d(x, y, z，scalars,…)  
scalars网格上的数据，用三维numpy数组表示。  x，y，z三维空间坐标    
   
|参数 |说明|
|---|---|
|contours |定义等值面的数量|
|transparent|对象是否透明表示。ture/flase|
  
##### 6、3D绘图函数-quiver3d()   
函数调用形式：    
quiver3d(u，v，w …)   
quiver3d(x，y，z，u，v，w …)   
quiver3d(x，y，z，f，…)   
u，v，w用numpy数组表示的向量   
x，y，z表示箭头的位置， u，v，w矢量元素  
f需要返回在给定位置（x，y，z）的（u，v，w）矢量  
  
### 改变物体的外观    
#### 改变颜色  
colormap定义的颜色，也叫LUT。  
LUT：Look Up Table。  
* 常见的colormaps      

||||||
|---|---|---|---|---|
|=accent |flag| hot| pubu |set2  |
|autumn |gist_earth| hsv| pubugn |set3 | 
|black-white| gist_gray| jet| puor| spectral|  
|blue-red| gist_heat |oranges| purd |spring|  
|blues| gist_ncar| orrd |purples |summer |  
|bone |gist_rainbow |paired| rdbu |winter|   
|brbg| gist_stern |pastel1 |rdgy| ylgnbu |  
|bugn |gist_yarg| pastel2 |rdpu ylgn   
|bupu| gnbu| pink| rdylbu| ylorbr  | 
|cool |gray| piyg| rdylgn |ylorrd |  
|copper| greens| prgn |reds |  
|dark2 |greys| prism |set1|   
  

[回到顶部](#readme)
  
--- 

### mlab控制函数   
#### 1、图像控制函数   

|函数名称 |说明|
|---|---|
|clf |清空当前图像 mlab.clf(figure=None)|
|close |关闭图像窗口 mlab.close(scene=None, all=False)|
|draw| 重新绘制当前图像mlab.close(figure=None)|
|figure|建立一个新的Scene或者访问一个存在的Scene。mlab.figure(figure=None,bgcolor=None,fgcolor=None,engine=None,size=(400,350))|
|gcf |返回当前图像的handle mlab.gcf(figure=None)|
|savefig|存储当前的前景，输出为一个文件，如png、jpg、bmp、tiff、pdf、obj、vrml等|

#### 2、图像装饰函数  

|函数名称 |说明|
|---|---|
|cololorbar |为对象的颜色映射增加颜色条。mlab.clolorbar(object=None, title=None,orientation=None, nb\_labels=None,nb\_colors=None, label\_fmt=None)|
|scalarbar 为对象的标量颜色映射增加颜色条|
|vectorbar |为对象的矢量颜色映射增加颜色条|
|xlabel |建立坐标轴，并添加x轴的标签mlab.xlabel(text, object=None)|
|ylabel| 建立坐标轴，并添加y轴的标签|
|zlabel |建立坐标轴，并添加z轴的标签|
  
#### 3、相机控制函数  

|函数名称 |说明|
|---|---|
|move| 移动相机和焦点。mlab.move(forward=None, right=None, up=None)|
|pitch| 沿着“向右”轴旋转角度mlab.pitch(degrees)|
|roll |设置/获取相机沿“向前”轴旋转一定角度。mlab.roll(roll=None, figure=None)|
|view| 设置/获取当前视图中相机的视点。mlab.view(azimuth=None, elevation=None，distance=None, focalpoint=None, roll=None, reset_roll=True, figure=None)|
|yaw| 沿着“向上”轴旋转一定角度，mlab.yaw(degrees)|
#### 4、其他控制函数  
|函数名称 |说明|
|---|---|
|animate|动画控制函数。mlab.animate(func=None, delay=500, ui=True)|
|axes |为当前物体设置坐标轴 mlab.axes(*args, **kwargs)|
|outline |为当前物体建立外轮廓 mlab.outline(*args, **kwargs)|
|**show **|与当前图像开始交互 mlab.show(func=None, stop=False)|
|show_pipeline|显示mayavi的管线对话框，可一进行场景属性的设置和编辑|
|text |为图像添加文本mlab.text(*args, **kwargs)|
|title |为绘制图像建立标题 mlab.title(*args, **kwargs)|
  
[回到顶部](#readme)

---

### 鼠标选取   
* 选取一个物体，查看数据  
* 选取物体上一点，查看数据  
响应鼠标事件:
`on\_mouse\_pick(callback, type=‘point’,Button=‘Left’,Remove=False)`  
选取类型Type:’point’,’cell’or ‘world’  
响应按键Button:’Left’,’Middle’or ‘Right’  
Remove:如果值为True，则callback函数不起作用  
返回：一个vtk picker 对象   
![](img\VTKpicker.png)  


---

### mlab管线控制函数  
#### Mlab管线控制函数的调用
mlab.pipeline.`function`()  
`Sources`：数据源   
`Filters`：用来数据变换  
`Modules`：用来实现可视化  
##### Sources:  
|函数名称 |说明|
|---|---|---|
|grid_source |建立二维网格数据|
|line_source |建立线数据|
|open |打开一个数据文件|
|scalar_field |建立标量场数据|
|vector_field |建立矢量场数据|
|volume_filed |建立体数据|

##### Filters:
不具备可视化功能，通常做为sources和modules的中介。mayavi中提供了32个参数   

|Filters |说明|
|---|---|
|contour |对输入数据集计算等值面|
|cut_plane |对数据进行切面计算，可以交互的更改和移动切面|
|delaunay2D |执行二维delaunay三角化|
|delaunay3D |执行三维delaunay三角化|
|extract\_grid |允许用户选择structured grid的一部分数据|
|extract\_vector\_norm |计算数据矢量的法向量，特别用于在计算矢量数据的梯度时|
|mask_points |对输入数据进行采样|
|threshold |取一定阈值范围内的数据|
|transform_data |对输入数据执行线性变换|
|tube |将线转成管线数据|
  
##### Modules:  
|Modules |说明|
|---|---|
|axes |绘制坐标轴|
|glyph |对输入点绘制不同类型的符号，符号的颜色和方向由该点的标量和适量数据决定。|
|image\_plane\_widget |绘制某一平面数据的细节|
|iso_surface |对输入的体数据绘制其等值面|
|outline |对输入数据绘制外轮廓|
|scalar\_cut\_plane |对输入的标量数据绘制特定位置的切平面|
|streamline |对矢量数据绘制流线|
|surface |对数据（VTK dataset，mayavi sources）建立外表面|
|text |绘制一段文本|
|vector\_cut\_plane |对输入的矢量数据绘制特定位置的切平面|
|volume |对标量场数据进行体绘制|
  
详细细节可参考：[Mlab Reference](http://docs.enthought.com/mayavi/mayavi/auto/mlab_reference.html)
  
---

[回到顶部](#readme)

---

# 叁、三维可视之交互界面   

## Traits基础  
* Traits库可以为Python添加类型定义  
* Traits属性解决color类型问题
    * 接收能表示颜色的各种类型的值  
    * 赋值不能表达颜色的值时，能立即捕捉到异常，并返回一个详细的使用报告
    * 提供一个内部、标准的颜色表达方式 `name.configure_traits()`提供一个可视化选择的交互界面。  

### Trait属性的功能    
Trait库为Python对象的属性增加了类型定义功能  
还提供了功能：  
* 初始化：每个Trait属性都有自己的默认值  
* 验证：Trait属性有明确的类型定义，满足定义的值才能赋值给属性  
* 代理：Trait属性值可以代理给其他对象的属性。  
* 监听：Trait属性值发生变化时，运行事先指定的函数  
* 可视化：拥有Trait属性的对象，可生成编辑Trait属性的界面    
### Trait属性监听
* 静态监听函数的几种形式：   
    * \_age\_changed(self)   
    * \_age\_changed(self, new)
    * \_age\_changed(self, old, new)   
    * \_age\_changed(self, name, old, new)   
* 动态监听函数的几种形式：   
    * observer()   
    * observer(new)   
    * observer(name, new)   
    * observer(obj, name, new)   
    * observer(obj, name, old, new)   
* Trait属性监听   
    * @on_trait_change(names)   
    * def any_method_name(self, …)   

### Event和Button属性  
* Event属性与其他Trait属性的区别:    
||Event属性| Trait属性|
|---|---|---|
|触发与其绑定的监听事件| 当任何值对Event属性赋值时；不存储属性值，所赋值将会被忽略；如果试图获取属性值会产生异常|   只有在值发生改变时|
|监听函数名| _event_fired()| _trait_changed()|
  
* Button属性：   
    * 具备Event事件处理功能  
    * 通过TraitsUI库,自动生成界面中的按钮控件  

### Property属性  
    from traits.api import Property    
  
---  
  
## [TraitUI库的基本使用](doc/TraitsUI入门.pdf)   
Python有着丰富的界面开发库  
* Tkinter（内嵌）  
* wxPython  
* pyQt4  
>需要程序员掌握众多的GUI、API函数：配置属性、位置、事件响应等函数，对于科学计算的应用来说，我们希望可以快速的开发界面，能够交互的处理程序，而不需花费很多精力在界面响应上。  
### TraitsUI  
* 以traits为基础  
* 以 MVC 为设计思想  
[TraitsUI文档](http://docs.enthought.com/traitsui/)  

``` Python 
TEST  
    fromtraits.api import HasTraits, Str, Int   
    //   
    class ModelManager(HasTraits):  
        model_name = Str    
        category = Str  
        model_file = Str  
        model_number = Int  
    //  
    model = ModelManager()  
    model.configure_traits()  
```

---
 
### View自定义  

#### traits.ui支持的后台界面库  
  
|后台界面库| 程序启动时选择界面库参数|
|---|---|
|qt4| -toolkit qt4|
|Wx |–toolkit wx|
  
#### 用View定义界面  
|MVC类别| MVC说明|
|---|---|
|Model |HasTraits的派生类用Trait保存数据，相当于模型|
|View| 没有指定界面显示方式时，Traits自动建立默认界面|
|Controller| 起到视图和模型之间的组织作用，控制程序的流程|
  
#### Item对象属性  
`from traitsui.api import View, Item`  
View模块描述了界面的示图类，Item模块描述了界面中的控件和模型对象Traits属性之间的关系的类。   
Item（id，name，label…）    
|属性| 说明|
|---|---|
|id| item的唯一id|
|name| trait属性的名称|
|label| 静态文本，用于显示编辑器的标签|
|tooltip| 编辑器的提示文本|
   
#### view对象属性    
View（title，width，height，resizable…）  

|属性 |说明|
|---|---|
|title| 窗口标题栏|
|Width |窗口宽度|
|Height| 窗口高度|
|resizable |窗口大小可变，默认为True|
  
---

### [Group对象组织界面](https://github.com/enthought/traitsui/blob/master/traitsui/group.py)   
#### Group对象
将一组相关的Item对象组织在一起,具有嵌套关系:  
`from traitsui.api import Group  `

|属性 |说明|
|---|---|
|orientation |编辑器的排列方向|
|layout |布局方式normal、flow、split、tabbed|
|show_labels| 是否显示编辑器的标签|
|columns| 布局的列数，范围为(1，50)|

  
#### Group的各种派生类     

|派生类 |说 明|
|---|---|
|HGroup |内容水平排列。Group(orientation=‘horizontal’)|
|HFlow |内容水平排列，超过水平宽度时，自动换行，隐藏标签文字。Group(orientation=‘horizontal’,layout=‘flow’,show_labels=False)|
|HSplit |内容水平分隔，中间插入分隔条。Group(orientation=‘horizontal’,layout=‘flow’)|
|Tabbed |内容分标签页显示。Group(orientation=‘horizontal’,layout=‘tabber’ )|
|VGroup |内容垂直排列。Group(orientation=‘vertical’)|
|VFlow |内容垂直排列，超过垂直高度时，自动换列，隐藏标签文字。Group(orientation=‘vertical’,layout=‘flow’,show\_labels=False)|
|VFold |内容垂直排列，可折叠。Group(orientation=‘vertical’,layout=‘fold’,show\_labels=False)|
|VGrid |按照多列网格进行垂直排列，columns属性决定网格的列数。Group(orientation=‘vertical’,columns=2)|
|VSplit| 内容垂直排列，中间插入分隔条。Group(orientation=‘vertical’,layout=‘split’)|
  


---

### 视图类型   

#### 通过kind属性设置View显示类型    
   
|显示类型 |说 明|
|---|---|
|modal |模态窗口，非即时更新|
|livemodal |模态窗口，即时更新|
|wizard |向导窗口，模态窗口，即时更新|
|live |非模态窗口，即时更新|
|nonmodal |非模态窗口，非即时更新|
|panel| 嵌入到其它窗口中的面板，即时更新，非模式，有自己的命令按钮|
|subpanel|嵌入窗口中的面板，没有命令按钮|
      
>**模态窗口：在此窗口关闭之前，其他窗口不能激活；**  
>**即时更新：修改控件内容，立即反应到模型数据上。**   
   
#### 调用使用时，有两类命令   

|configure\_traits |edit\_traits()|
|---|---|
界面显示后，进入消息循环 |界面显示后，不进入消息循环。|
|主界面窗口或模态对话框 |无模态窗口或对画框|


----
----


~~[TraitUI与Mayavi结合实例](doc/TraitsUI与Mayavi应用实例.pdf)~~

  
---  
[回到顶部](#readme)    
  
---  
  
  

# 四、三维可视之运算    
~~**[SciPy库的介绍和拟合与统计运算](doc/Scipy基础一.pdf)**  
**[SciPy库的线性代数、积分和差值等运算](Scipy基础二.pdf)**  
**[SciPy库实例](Scipy可视化实例.pdf)**~~  
