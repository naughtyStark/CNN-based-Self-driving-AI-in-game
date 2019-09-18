import numpy as np
from sidnet import alexnet

WIDTH = 80
HEIGHT = 60
LR = 0.0005
EPOCH = 10
MODEL_NAME ='SIDNET_-{}-{}-{}-{}-{}.model'.format(0.001,'sidnet',EPOCH,'FORZA','throttle')
# MODEL_NAME ='SIDNET_-{}-{}-{}-{}-{}.model'.format(LR,'sidnet',EPOCH,'FORZA','steering')


model = alexnet(HEIGHT,WIDTH,LR)
model.load(MODEL_NAME)

train_data = np.load('FORZA_160x120_separate_corners.npy')
train_data = train_data[0]

train = train_data[:-8000]
test = train_data[-8000:]

# #this is for throttle
X= np.array([i[0] for i in train])
Y= [i[1][:2] for i in train]
test_x = np.array([i[0] for i in test])
test_y = [i[1][:2] for i in test]

#this is for steering
# X= np.array([i[0] for i in train])
# Y= [i[1][2:] for i in train]
# test_x = np.array([i[0] for i in test])
# test_y = [i[1][2:] for i in test]

model.fit({'input':X},{'targets':Y},n_epoch = EPOCH,
          validation_set=({'input':test_x},{'targets':test_y}),
          snapshot_step=500,show_metric = True, run_id= MODEL_NAME)
#tensorboard --logdir=foo:C:/Python35/log

model.save(MODEL_NAME)
