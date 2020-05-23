import numpy as np
from sidnet import MUSHR
import tflearn
import cv2
import time

WIDTH =  320
HEIGHT = 240
LR = 0.01
EPOCH = 1

MODEL_NAME ='MUSHR_-{}-{}-{}-{}.model'.format(LR,'TRAJ',EPOCH,'steering')

model = MUSHR(HEIGHT,WIDTH,LR)
model.load(MODEL_NAME)

output_path = "C:/Python37/DonkeySimWin/Outputs"
counter = 0
for i in range(1):
      train_data = np.load('MUSHR_320x240_shuffled_{}.npy'.format(str(i)),allow_pickle=True)

      X = np.array([i[0].reshape(HEIGHT,WIDTH,1) for i in train_data])
      Y = np.array([i[1].reshape(HEIGHT,WIDTH,1) for i in train_data])

      for j in range(0,len(X),1000):
            img = X[j]
            expected = Y[j]
            now = time.time()
            traj = (model.predict([img])[0]*255)
            dt = time.time()-now
            print(dt*1000)
            # added_image = cv2.addWeighted(img,0.0,traj,1.0,0)
            # added_image = cv2.addWeighted(added_image,0.8,expected,0.5,0)
            cv2.imwrite(output_path+"/{}.jpg".format(str(counter)),traj)
            counter += 1
      inputs = None
      del inputs
      output = None
      del output

