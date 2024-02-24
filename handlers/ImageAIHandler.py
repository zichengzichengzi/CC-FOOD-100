from tornado.web import RequestHandler
from tornado import gen
#from deeplab.deeplab import model_pojo
from yolov8.yolo import yolov8
import numpy as np
import requests
from PIL import Image
import base64
from io import BytesIO
import re
from utils.cal_vol import calculate,calculate_volume

color_name = ['red','green','blue','light']
#classes_name = ['back','gaifan','noodle','doujiang','rice','gui','xiaomi','mizhou','tang','baozi','egg','youtiao','circle','triangle','mantou','dumpling','huntun','shala','youzha','chaofan']
classes_name=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '57', '59', '60', '62', '66', '68', '70', '72', '73', '74', '76', '79', '81', '82', '85', '86', '87', '89', '91', '92', '95', '96', '98', '100', '104', '106', '112', '113', '121', '122', '124', '125', '126', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '160', '161', '162', '163', '164', '165', '166', '168', '169', '171', '172', '173', '175', '177', '178', '184', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '207', '209', '210']
class ImageAIHandler(RequestHandler):
    def Image2base64(self,img):
        output_buffer = BytesIO()
        img.save(output_buffer, format='JPEG')
        byte_data = output_buffer.getvalue()
        base64_byte = base64.b64encode(byte_data)
        return base64_byte.decode('utf-8')
    def base642Image(self,img):
        base64_data = re.sub('^data:image/.+;base64,', '', img.decode('utf-8'))
        byte_data = base64.b64decode(base64_data)
        image_data = BytesIO(byte_data)
        img = Image.open(image_data)
        return img
    @gen.coroutine
    def post(self):
        userid = self.get_argument('userId','none')
        rgb_img = self.request.files['rgb'][0]
        depth_img = self.request.files['depth'][0]
        img = self.base642Image(rgb_img['body'])
        depth_img = np.frombuffer(depth_img['body'], dtype=np.uint16)
        depth_img = depth_img.reshape((480,640))
        # print(depth_img.shape)
        #show_img,seg_img,num_classes = model_pojo.detect_image(img)
        show_img, num_classes = yolov8.detect_image(img)
        show_img.show()
        #seg_img = np.array(seg_img)
        #classes_volume = calculate(depth_img,seg_img,num_classes)
        classes_volume = []
        for i in range(len(num_classes)):
            classes_volume.append(1)
        data_num = calculate_volume(num_classes,classes_volume,classes_name,color_name)
        show_img = self.Image2base64(show_img)
        # print(data_num)
        # print(userid)
        if userid!='':
            r = requests.post('http://39.96.88.193/api/food/synUserMeals',data = {'userId':userid,'meals':str(data_num)})
        # print(r.text)
        self.finish({'show_img':show_img,'data_num':data_num,"num_classes":num_classes})
    @gen.coroutine
    def get(self):
        print('ok1')
        
        self.finish('asd1')
