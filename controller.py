import serial
import time
import pyxinput
import numpy as np

ser =  serial.Serial('COM4', 250000, timeout=0)

if ser.isOpen():
    ser.close()
ser.open()

steering = 1500
throttle = 1500

controller = pyxinput.vController()

t=s=AxisRx=A=B=0

control_file = 'data_file.npy'
input_file = 'input_file.npy'

while 1:
    while(ser.inWaiting()<10):
        pass
    #print(steering)
    steering = ord(ser.read())<<8|ord(ser.read())
    throttle = ord(ser.read())<<8|ord(ser.read())
    right_stick = ord(ser.read())<<8|ord(ser.read())
    A = ord(ser.read())<<8|ord(ser.read())
    B = ord(ser.read())<<8|ord(ser.read())
    s = (steering - 1500)*0.004
    t = (throttle - 1500)*0.0018
    AxisRx = (right_stick-1500)*0.002 
    #prevent steering and throttle from being outside the usable range.
    if(B>1500):
        for i in range(10):
            try:
                data = np.load(input_file)
                s = data[0]
                t = data[1]
                break
            except:
                time.sleep(0.001)
                pass    

    if s>1.0 :
        s = 1.0
    elif s<-1.0:
        s = -1.0
    if t>1.0:
        t = 1.0
    elif t<-1.0:
        t = -1.0
    # print(s,t)

            #set the steering and throttle 
    controller.set_value('AxisLx',s)
    if t>=0.0:
        controller.set_value('TriggerR',t)
        controller.set_value('TriggerL',0.0)
        # controller.set_value('BtnA',0.0)
    elif t<0.0:
        controller.set_value('TriggerR',0)
        controller.set_value('TriggerL',-t)
        # controller.set_value('BtnA',1.0)    
    if(A>1500):
        controller.set_value('BtnA',1)
    elif(A<1500):
        controller.set_value('BtnA',0)
    if(B>1500):
        controller.set_value('BtnB',1)
    elif(B<1500):
        controller.set_value('BtnB',0)
    if(AxisRx>0.8):
        controller.set_value('BtnY',1)
    elif(AxisRx<0.8):
        controller.set_value('BtnY',0)
    # print(s, t)
    np.save(control_file,np.array([s,t]))

def control_write(s_input,t_input):
    while(ser.inWaiting()<10):
        pass
    steering = ord(ser.read())<<8|ord(ser.read())
    throttle = ord(ser.read())<<8|ord(ser.read())
    right_stick = ord(ser.read())<<8|ord(ser.read())
    A = ord(ser.read())<<8|ord(ser.read())
    B = ord(ser.read())<<8|ord(ser.read())
    learn = False
    if(B>1500):
        s = (steering - 1500)*0.004
        t = (throttle - 1500)*0.0018
        learn = True
    else:
        s = s_input
        t = t_input
    AxisRx = (right_stick-1500)*0.002 
    #prevent steering and throttle from being outside the usable range.
    if s>1.0 :
        s = 1.0
    elif s<-1.0:
        s = -1.0
    if t>1.0:
        t = 1.0
    elif t<-1.0:
        t = -1.0
    controller.set_value('AxisLx',s)
    if t>=0.0:
        controller.set_value('TriggerR',t)
        controller.set_value('TriggerL',0.0)
    elif t<0.0:
        controller.set_value('TriggerR',0)
        controller.set_value('TriggerL',-t)
    if(A>1500):
        controller.set_value('BtnA',1)
    elif(A<1500):
        controller.set_value('BtnA',0)
    if(B>1500):
        controller.set_value('BtnB',1)
    elif(B<1500):
        controller.set_value('BtnB',0)
    if(AxisRx>0.8):
        controller.set_value('BtnY',1)
    elif(AxisRx<0.8):
        controller.set_value('BtnY',0)
    return s,t,learn

