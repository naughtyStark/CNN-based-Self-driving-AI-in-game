import numpy as np
from sidnet import MUSHR
import tflearn
import time
WIDTH =  320
HEIGHT = 240
LR = 0.01
EPOCH = 1

MODEL_NAME ='MUSHR_-{}-{}-{}-{}.model'.format(LR,'TRAJ',EPOCH,'steering')

# tflearn.init_graph(num_cores=1, gpu_memory_fraction=0.1)
# model = alexnet(HEIGHT,WIDTH,LR)
model = MUSHR(HEIGHT,WIDTH,LR)
# model.load(MODEL_NAME)

for i in range(1):
	for k in range(4):
		train_data = np.load('MUSHR_320x240_shuffled_{}.npy'.format(str(k)),allow_pickle=True)

		# X = np.array([i[0].reshape(HEIGHT,WIDTH,1) for i in train_data])
		# Y = np.array([i[1].reshape(HEIGHT,WIDTH,1) for i in train_data])

		model.fit(train_data[:,0].reshape(train_data[:,0].shape[0],HEIGHT,WIDTH,1), train_data[:,1].reshape(train_data[:,0].shape[0],HEIGHT,WIDTH,1)>128, n_epoch = EPOCH,
		          validation_set=0.1,batch_size=16,
		          snapshot_step=500,show_metric = True, run_id= MODEL_NAME)

		del train_data
		time.sleep(5)
#tensorboard --logdir=foo:C:/Python35/log
	model.save(MODEL_NAME)
