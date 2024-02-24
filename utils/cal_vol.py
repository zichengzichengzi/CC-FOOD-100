import numpy as np
import open3d as o3d
import sqlite3

fx=609.259
fy=610.283
px=319.615
py=242.727
Z_plane=0.5
result=0.0
intrinsics_matrix=np.matrix([[fx,0,px],[0,fy,py],[0,0,1]],dtype=np.float32)
def calculate(depth_array,mask,numclasses):
    pixel_coordinates_array=[[] for i in numclasses]
    depth_temp=[[] for i in numclasses]
    return_array=[]
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i,j] in numclasses:
                pixel_coordinates_array[numclasses.index(mask[i,j])].append([j,i,1])
                depth_temp[numclasses.index(mask[i,j])].append(depth_array[i,j])
    for i in range(len(pixel_coordinates_array)):
        result=0.0
        temp1=np.array(depth_temp[i])
        temp=np.array(pixel_coordinates_array[i]).T
        temp=np.matrix([[1,0,0],[0,-1,0],[0,0,-1]])*intrinsics_matrix.I*(temp*temp1)/1000
        # handle the points 
        pointcloud = o3d.geometry.PointCloud()
        pointcloud.points = o3d.utility.Vector3dVector(np.asarray(temp.T))
        pointcloud=pointcloud.voxel_down_sample(voxel_size=0.001)#单位面积1平方毫米
        points=np.asarray(pointcloud.points)
        for i in range(points.shape[0]):
            result+=abs(Z_plane+points[i][2])
        result-=result*0.3
        return_array.append(result)
    return return_array

dict_color = {"red":"红色", "green":"绿色", "blue":"蓝色", "light":"青色"}

fr=open("./database/index.txt",'r',encoding='UTF-8')
keys=fr.read().splitlines()
fr.close()
fr1=open("./database/name.txt",'r',encoding='UTF-8')
values=fr1.read().splitlines()
fr1.close()

dict_class = dict(zip(keys,values))#稍微修改一下输出的名称
print(dict_class)
def calculate_volume(num_classes,classes_volume,classes_name,color_name):
    # sql ops to find the nutrition of the food pre unit
    name = []
    density = []
    calorie = []
    fat= []
    protein=[]
    carbon=[]
    cellulose=[]
    conn = sqlite3.connect('./database/food.db')
    c = conn.cursor()
    for i in num_classes:
        cursor = c.execute("SELECT name,density,calorie,fat,protein,carbon,cellulose from food WHERE name=('%s')"%(i))
        for row in cursor:
            name.append(row[0])
            density.append(row[1])
            calorie.append(row[2])
            fat.append(row[3])
            protein.append(row[4])
            carbon.append(row[5])
            cellulose.append(row[6])
    conn.close()
    

    #定义存储变量
    color_name_total_list = []
    attribute_total_list = []

    for i in range(len(name)):
        #添加color和name
        color_name_list = []
        color_name_list.append(dict_color[color_name[i]])
        color_name_list.append(dict_class[name[i]])
        color_name_total_list.append(color_name_list)

        #添加相关属性数据
        attribute_list = []
        #质量
        attribute_list.append(density[i]*classes_volume[i])
        #卡路里
        attribute_list.append(calorie[i]*classes_volume[i])
        #脂肪
        attribute_list.append(fat[i]*classes_volume[i])
        #蛋白质
        attribute_list.append(protein[i]*classes_volume[i])
        #碳水
        attribute_list.append(carbon[i]*classes_volume[i])
        #纤维素
        attribute_list.append(cellulose[i]*classes_volume[i])
        if len(attribute_list)!=0:
            attribute_list.append(1.0)
        attribute_total_list.append(attribute_list)
    return [color_name_total_list,attribute_total_list]