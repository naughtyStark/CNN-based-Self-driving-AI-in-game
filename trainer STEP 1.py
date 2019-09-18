#convert the actions to a one hot array
import numpy as np
import cv2
from PIL import ImageGrab
from key_check import key_check,key_press
import os
import time
import math as m
# os.system('python controller.py')
file_name = 'FORZA_160x120_separate_6.npy'

if os.path.isfile(file_name):
    # print('File exists, loading..')
    training_data = list(np.load(file_name))
else:
    # print('file does not exist,starting fresh ')
    training_data = []

control_file = 'data_file.npy'

def draw_hsv(flow_x,flow_y,img1, img2,map_speed):
    h, w = flow_x.shape
    bgr = np.zeros((h,w,6),np.uint8)
    flow_x_pos = np.maximum(flow_x,np.zeros_like(flow_x))
    bgr[...,0] = np.array(2*flow_x_pos,dtype = np.uint8)
    flow_x_neg = np.maximum(-flow_x,np.zeros_like(flow_x))
    bgr[...,1] = np.array(2*flow_x_neg,dtype = np.uint8)
    flow_y_pos = np.maximum(flow_y,np.zeros_like(flow_x))
    bgr[...,2] = np.array(2*flow_y_pos,dtype = np.uint8)
    bgr[...,3] = img1
    bgr[...,4] = img2
    bgr[...,4] = map_speed
    return bgr

def main():
    for i in list(range(10))[::-1]:
        print(i+1)
        time.sleep(1)
    last_time=time.time()
    last_t = last_s = 0.5
    paused = False
    now = time.time()
    prevgray = np.array(ImageGrab.grab(bbox=(0,200,1280,800)))
    prevgray = prevgray[250:450,:]
    prevgray = cv2.cvtColor(prevgray,cv2.COLOR_BGR2GRAY)
    prevgray = cv2.resize(prevgray,(160,120))
    _a = cv2.resize(prevgray, (80,60))
    dummy = np.array([_a, _a, _a, _a])

    while True:
        if not paused:
            now = time.time()
            img = np.array(ImageGrab.grab(bbox=(0,200,1280,800)))
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            map_img = img[520:600,107:167]
            map_img = cv2.resize(map_img,(40,60))
            speed_img = img[450:600,1080:1200]
            speed_img = cv2.resize(speed_img,(40,60))
            map_speed = np.concatenate((map_img,speed_img),axis=1)#width = 80, height = 60
            
            img = img[250:450,:]
            img = cv2.resize(img,(160,120))
            flow = cv2.calcOpticalFlowFarneback(prevgray, img,None, 0.5, 3, 15, 3, 5, 1.2, 0)
            prevgray = img
            flow_x = cv2.resize(flow[:,:,0],(80,60))
            flow_y = cv2.resize(flow[:,:,1],(80,60))
            img = cv2.resize(img,(80,60))
            dummy[0],dummy[1],dummy[2],dummy[3] = img, dummy[0], dummy[1], dummy[2]
            img = draw_hsv(flow_x,flow_y, dummy[0], dummy[3],map_speed)
            for i in range(10):
                try:
                    data = np.load(control_file)
                    s = data[0]
                    t = data[1]
                    break
                except:
                    time.sleep(0.0001)
                    pass
            print(len(training_data))

            l = 0.5*(1-s)
            r = 0.5*(1+s) 

            f = 0.5*(1+t)
            b = 0.5*(1-t)


            keys = np.array([f,b,l,r])
            # if(l>0.95 or r>0.95):
            #     # print("--")
            #     for i in range(10):
            #         training_data.append([img,keys])
            # if(b>0.5 or f>0.7):
            #     for i in range(10):
            #         training_data.append([img,keys])
            training_data.append([img,keys])

            if len(training_data)% 500 == 0:
                print(len(training_data))
            while(time.time()-now<0.0666):
                pass

        if(key_press() == ['O'] ):
            print("recording aborted")
            break
        if(key_press() == ['K'] ):
            if paused:
                print("recording continued")
                paused = False
                time.sleep(0.5)

            elif not paused :
                print("recording paused")
                paused = True
                time.sleep(0.5)
    return training_data
        
training_data = main()
np.save(file_name,training_data)
    
                















