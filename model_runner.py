import numpy as np 
import time
from sidnet import alexnet 
from key_check import key_check,key_press
import math as m 
import tensorflow as tf 

WIDTH = 80
HEIGHT = 60
LR = 0.0001
EPOCH = 10
MODEL_NAME_THROTTLE ='SIDNET_-{}-{}-{}-{}-{}.model'.format(0.001,'sidnet',EPOCH,'FORZA','throttle')
MODEL_NAME_STEERING ='SIDNET_-{}-{}-{}-{}-{}.model'.format(0.0005,'sidnet',EPOCH,'FORZA','steering')

tf.reset_default_graph()
model_throttle = alexnet(HEIGHT,WIDTH,LR)
model_throttle.load(MODEL_NAME_THROTTLE,weights_only=True)

tf.reset_default_graph()
model_steering = alexnet(HEIGHT,WIDTH,LR)
model_steering.load(MODEL_NAME_STEERING,weights_only=True)


control_file = 'input_file.npy'
output_file = 'output_file.npy'


def main():
      while(True):
            paused = False
            if not paused:
                  now = time.time()
                  for i in range(10):
                        try:
                              img = np.load(output_file)
                              break
                        except:
                              time.sleep(0.001)
                  prediction = model_throttle.predict([img])[0]#prediction is the 0th index output of the model output
                  f = prediction[0]
                  b = prediction[1]
                  prediction = model_steering.predict([img])[0]
                  l = prediction[0]
                  r = prediction[1]
                  # print(f,b,l,r,scale)
                  t = (f-b)
                  s = (r-l)#left is -ve
                  # if(m.fabs(s)<=0.1):
                  #       s *= 3
                  # if(s>0.1):
                  #       s = 0.3 + 0.7*s/0.9
                  # if(s<-0.1):
                  #       s = -0.3 + 0.7*s/0.9

                  print(s,t)
                  np.save(control_file,np.array([s,t]))
                  while(time.time()-now<0.09):
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
main()
