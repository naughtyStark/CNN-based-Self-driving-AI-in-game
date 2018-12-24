
import numpy as np
from sidnet import alexnet

WIDTH = 160
HEIGHT = 60
LR = 0.001
EPOCH = 5
MODEL_NAME ='SIDNET_tanh-{}-{}-{}-{}.model'.format(LR,'alexnet',EPOCH,'nissan_GTR')

model = alexnet(WIDTH,HEIGHT,LR)
#model.load('SIDNET_SQ-0.0001-alexnet-8-nissan_GTR.model')

train_data = np.load('training_data_converted_balanced.npy')

train = train_data[:-2000]
test = train_data[-2000:]

X= np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y= [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

model.fit({'input':X},{'targets':Y},n_epoch = EPOCH,
          validation_set=({'input':test_x},{'targets':test_y}),
          snapshot_step=500,show_metric = True, run_id= MODEL_NAME)
#tensorboard --logdir=foo:C:/Python35/log

model.save(MODEL_NAME)
