from __future__ import print_function
import requests
import json
import cv2
import find
from PIL import Image

url = 'http://localhost:5000'

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

img = cv2.imread('./image/Asad_test.jpg')


find.face_rec(img)


'''
# encode image as jpeg
_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
response = requests.post(url, data=img_encoded.tostring(), headers=headers)
# decode response
print(json.loads(response.text))
'''
# expected output: {u'message': u'image received. size=124x124'}