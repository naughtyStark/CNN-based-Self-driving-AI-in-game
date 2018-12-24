#convert the actions to a one hot array
import numpy as np
import cv2
from PIL import ImageGrab
from key_check import key_check,key_press
import os
import time
##import HAL_read
##from HAL_read import input_reader
import control_reader
from control_reader import input_reader
file_name = 'training_data_nissan_GTR_160X60_4.npy'

if os.path.isfile(file_name):
    print('File exists, loading..')
    training_data = list(np.load(file_name))
    
else:
    print('file does not exist,starting fresh ')
    training_data = []


def main():
    for i in list(range(10))[::-1]:
        print(i+1)
        time.sleep(1)
    last_time=time.time()
    last_t = last_s = 0.5
    paused = False
    while True:
        if not paused:
            img = np.array(ImageGrab.grab(bbox=(0,40,1024,768)))
            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            road_map = img[580:640,90:170]
            img = cv2.resize(img,(80,60))
            img = np.concatenate((img,road_map),axis=1)
            #final image is of dimensions width,height=160,60
            t,s = input_reader()
            
##            s = float((s + 9*last_s)/10)
##            #print(keys)
##            last_t = t
##            last_s = s
            
            if  s<=0.5:
                l = 2*(0.5-s)
                l = l**(0.5)
                r = 0
                
            if  t>=0.5:
                f = 2*(t-0.5)
                f = f**(0.5)
                b = 0

            if  s>0.5:
                r = 2*(s-0.5)
                r = r**(0.5)
                l = 0
            
            if  t<0.5:
                f = 0
                b = 2*(0.5-t)
                b = b**(0.5)

            keys = np.array([f,b,l,r])
            training_data.append([img,keys])

            if len(training_data)% 500 == 0:
                print(len(training_data))

        if(key_press() == ['Q'] ):
            print("recording aborted")
            break
        if(key_press() == ['P'] ):
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
    
                















