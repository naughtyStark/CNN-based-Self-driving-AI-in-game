import serial
import time
import pyxinput

ser =  serial.Serial('COM5', 250000, timeout=0)

if ser.isOpen():
    ser.close()
ser.open()

steering = 1500
throttle = 1500

controller = pyxinput.vController()

t=s=AxisRx=A=B=0

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
    if s>1.0 :
        s = 1.0
    elif s<-1.0:
        s = -1.0
    if t>1.0:
        t = 1.0
    elif t<-1.0:
        t = -1.0

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

