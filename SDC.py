import numpy as np 
from PIL import ImageGrab
import cv2
import time
from key_check import key_check,key_press
import math as m 


control_file = 'input_file.npy'
output_file = 'output_file.npy'

def draw_hsv(flow_x,flow_y,img,map_speed):
    h, w = flow_x.shape
    bgr = np.zeros((h,w,5),np.uint8)
    flow_x_pos = np.maximum(flow_x,np.zeros_like(flow_x))
    bgr[...,0] = np.array(2*flow_x_pos,dtype = np.uint8)
    flow_x_neg = np.maximum(-flow_x,np.zeros_like(flow_x))
    bgr[...,1] = np.array(2*flow_x_neg,dtype = np.uint8)
    flow_y_pos = np.maximum(flow_y,np.zeros_like(flow_x))
    bgr[...,2] = np.array(2*flow_y_pos,dtype = np.uint8)
    bgr[...,3] = img
    bgr[...,4] = map_speed
    return bgr

def main():
    lasts=0
    paused = False
    prevgray = np.array(ImageGrab.grab(bbox=(0,200,1280,800)))
    prevgray = prevgray[250:450,:]
    prevgray = cv2.cvtColor(prevgray,cv2.COLOR_BGR2GRAY)
    prevgray = cv2.resize(prevgray,(160,120))
    while(True):
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
        img = draw_hsv(flow_x,flow_y,img,map_speed)
        
        for i in range(10):
            try:
                np.save(output_file,img)
                break
            except:
                time.sleep(0.001)

        delta = time.time()-now
        # print(delta)
        while(time.time()-now<0.09):
            pass
            
main()
