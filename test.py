#convert the actions to a one hot array
import numpy as np
import cv2
from PIL import ImageGrab
from key_check import key_check,key_press
import os
import time
# time.sleep(5)

# img = np.array(ImageGrab.grab(bbox=(0,200,1280,800)))
original_img = cv2.imread('test.jpg')
now = time.time()
img = cv2.cvtColor(original_img,cv2.COLOR_BGR2GRAY)
map_img = img[520:600,107:167]
map_img = cv2.resize(map_img,(40,60))
# print(map_img.dtype)
map_img = np.array(map_img,dtype=np.uint8)
speed_img = img[450:600,1080:1200]
speed_img = cv2.resize(speed_img,(40,60))
speed_img = np.array(speed_img,dtype=np.uint8)
map_speed = np.concatenate((map_img,speed_img),axis=1)
# print(map_speed.shape)
# img = cv2.resize(img,(80,60))
img = img[250:450,:]
flow = cv2.calcOpticalFlowFarneback(img, img,None, 0.5, 3, 15, 3, 5, 1.2, 0) #calculate flow
img =  cv2.resize(img,(80,60))
# print(img.dtype)
flow = cv2.resize(flow,(160,120))
img = np.array(img,dtype = np.uint8)
delta = time.time() - now
print(delta/100)

cv2.namedWindow('window',cv2.WINDOW_NORMAL)
cv2.resizeWindow('window',400,300)

cv2.imshow('window',map_speed)
cv2.waitKey(0)
# cv2.imwrite('test.jpg',img)
cv2.destroyAllWindows()

    
                















