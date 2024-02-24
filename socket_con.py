import requests
from PIL import Image
import base64
from io import BytesIO
import re
import json
import numpy as np
def base642Image(img):
    base64_data = re.sub('^data:image/.+;base64,', '', img)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    return img
img = Image.open('/home/fanrencli/Desktop/asd.png')
depth = np.load('/home/fanrencli/Desktop/asd.npy')
output_buffer = BytesIO()
img.save(output_buffer, format='JPEG')
byte_data = output_buffer.getvalue()
base64_str = base64.b64encode(byte_data)
print(depth.shape)


data_json = {'userid':'123123123'}
files = {'rgb':base64_str,'depth':depth.tobytes()}
url = 'http://127.0.0.1:8080/image'
r = requests.post(url,data = {'userId':'222222'},files = files)
# print(r.text)
asd = json.loads(r.text)
show_img = base642Image(asd['show_img'])
# seg_img = base642Image(asd['seg_img'])
list1 = asd['data_num']
print(list1)
show_img.show()
# seg_img.show()
