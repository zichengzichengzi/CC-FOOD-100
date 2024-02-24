# CC-FOOD-100
a new food dataset(rgb+depth) CC Food-100 for food detection and nutrient calculation. The dataset has been collected in real college canteen in China. Depth images are raw data that can be used for food volume calculation or other downstream tasks.
![微信截图_20240126223709](https://github.com/zichengzichengzi/CC-FOOD-100/assets/43312794/281d479d-2be6-4ff9-a017-2d02b2e9b25e)
![微信截图_20240126223722](https://github.com/zichengzichengzi/CC-FOOD-100/assets/43312794/d52b8b55-fc70-4512-8050-7802e1241b9d)


|名称|下载地址|
|:---|:---|
|CC-FOOD-100|https://pan.baidu.com/s/1Cb4AULANrZSCKgsg10XFaQ password:9ucz|

## Dataset structure

```
|-- <CC-FOOD-100>
    |-- <json> 存放标签文件
        0.json
        1.json
        ...
    |-- <depth>存放深度图像文件
        0.png
        1.png
        ...
    |-- <rgb>存放彩色图像文件
        0.png
        1.png
        ...
        
```

--- 

## Food image analysis server
We provide food image analysis server source for food recognition and nutrient estimation.
### Requirements
* Python 3.7+
* PyTorch 1.7.0 or higher
* CUDA 10.2 or higher
* Open3D 0.17 or higher
* sqlite3 3.17 or higher
* tornado 1.6.2 or higher
