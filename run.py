from tornado.web import Application
from os.path import sys,dirname,abspath
import threading
import tornado.ioloop
import time
import sys
from handlers.ImageAIHandler import *
# 添加系统路径变量
dirpath=dirname(abspath(__file__))
sys.path.append(dirpath)
if __name__ == "__main__":

    img1 = Image.open('./536.jpg')
    show_img, num_classes = yolov8.detect_image(img1)
    classes_volume = []
    for i in range(len(num_classes)):
        classes_volume.append(1)
    data_num = calculate_volume(num_classes, classes_volume, classes_name, color_name)
    show_img.show()
    print(num_classes)
    print(data_num)


    app = Application([(r'/image',ImageAIHandler)])
    #绑定一个监听端口
    app.listen(8080)
    #启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()