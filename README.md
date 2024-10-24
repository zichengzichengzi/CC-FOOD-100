# CC-FOOD-100
a new food dataset(rgb+depth) CC Food-100 for food detection and nutrient calculation. The dataset has been collected in real college canteen in China. Depth images are raw data that can be used for food volume calculation or other downstream tasks.
![微信截图_20240126223709](https://github.com/zichengzichengzi/CC-FOOD-100/assets/43312794/281d479d-2be6-4ff9-a017-2d02b2e9b25e)
![微信截图_20240126223722](https://github.com/zichengzichengzi/CC-FOOD-100/assets/43312794/d52b8b55-fc70-4512-8050-7802e1241b9d)


|Name|Address|
|:---|:---|
|CC-FOOD-100|[https://pan.baidu.com/s/1Cb4AULANrZSCKgsg10XFaQ password:9ucz](https://pan.baidu.com/s/1o7ZDwkd4oUFui5UZMmIvPw?pwd=pfav)|

## Dataset structure

```
|-- <CC-FOOD-100>
    |-- <json> //Store label files
        0.json
        1.json
        ...
    |-- <depth> //Store depth images
        0.npy
        1.npy
        ...
    |-- <rgb> //Store color images
        0.png
        1.png
        ...
    |-- <xml> //Store voc xml
        0.xml
        1.xml
        ...
        
```
@article{GAO2024141739,
title = {A vision-based dietary survey and assessment system for college students in China},
journal = {Food Chemistry},
pages = {141739},
year = {2024},
issn = {0308-8146},
doi = {https://doi.org/10.1016/j.foodchem.2024.141739},
url = {https://www.sciencedirect.com/science/article/pii/S0308814624033892},
author = {Zicheng Gao and Xufeng Yuan and Jie Lei and Hao Guo and Francesco Marinello and Lorenzo Guerrini and Alberto Carraro},
keywords = {Nutritional intake analysis, RGB-D image, College students' dietary habits, Automated food recognition, Volume estimation},
abstract = {Understanding the current dietary habits of college students is essential due to the pressing issues of unbalanced diets and insufficient nutrition. However, traditional approaches frequently depend on recollection, which can introduce unconscious bias and make them difficult to implement. Herein, we introduce a new computer vision system to evaluate the dietary habits of college students in China. A specialized food dataset comprising RGB-D images, recipes with ingredient masses, and nutrient composition was created using data collected from college canteens. First, object detection models were utilized to identify food categories and locations. Subsequently, we introduced a method for automatically estimating the food volume of nonstandard portions using position and depth information. The final nutrients were derived directly or indirectly through the database. Experimental results demonstrate the applicability of the YOLOv8 object detection model and volume estimation method to our tasks. To support the development of devices for detecting food intake and diet management, we have made our dataset publicly available. The College Canteen Food-100 dataset is publicly available at https://github.com/zichengzichengzi/CC-FOOD-100.}
}

--- 


