import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
import time


data0 = np.load('FORZA_160x120_separate_0.npy')[0]
shuffle(data0)
data1 = np.load('FORZA_160x120_separate_1.npy')[0]
shuffle(data1)
data2 = np.load('FORZA_160x120_separate_2.npy')[0]
shuffle(data2)
data3 = np.load('FORZA_160x120_separate_corners.npy')[0]
shuffle(data3)
print(data0.shape,data1.shape,data2.shape,data3.shape)
data = np.concatenate((data0,data1,data2,data3),axis=0)
shuffle(data)
print(data.shape)
data = np.array([data])
# print(data.shape)
np.save('FORZA_160x120_separate_final.npy',data)
# shuffle(data0)
# data1 = np.load('FORZA_160x120_1.npy')[0]
# data2 = np.load('FORZA_160x120_2.npy')[0]
# data3 = np.load('FORZA_160x120_3.npy')[0]
# data4 = np.load('FORZA_160x120_4.npy')[0]
# print(data1.shape,data2.shape,data3.shape,data4.shape)

# # shuffle(data1)
# # data2 = np.load('FORZA_160x120_2.npy')
# # shuffle(data2)

# # print(data1.shape[0])
# # print(data1.shape,data2.shape)
# data = np.concatenate((data1,data2,data3,data4),axis=0)
# print(data.shape)
# # print(data3.shape)
# # data3 = data3[0]
# # shuffle(data3)
# # data3 = np.array([data3])
# # print(data3.shape)
# # np.save('FORZA_160x120_atan.npy',data3)

# # train_data = np.load('FORZA_160x120_0.npy')
# # train_data = train_data[0]

# # Y= [i[1] for i in train_data]
# # Y = np.array(Y)
# # Y = np.arctan(Y)
# # Y *= 10

# # print(Y[:10])

# # to verify 
# # for i in range(train_data.shape[0]):
# #     img = train_data[i][0]
# #     print(img.shape)
# #     # choice = data[1]
# #     cv2.imshow('test',img)
# #     # print(choice)
# #     if cv2.waitKey(25) & 0xFF == ord('q'):
# #         cv2.destroyAllWindows()
# #         break

# # df = pd.DataFrame(train_data)
# # #this counts the number of forward, left and right
# # print(Counter(df[1].apply(str)))

# lefts = []
# rights = []
# forwards = []
# brakes = []
# # null =[]

# # #since we are not using LSTM cell
# # #so the order doesn't matter here
# # c =0
# for i in range(data.shape[0]):
#     img = data[i][0]
#     choice = data[i][1]

#     f = choice[0]
#     b = choice[1]
#     l = choice[2]
#     r = choice[3]
#     choice = np.array([f,b,l,r,0.1])
    
#     if  l>0:
#         lefts.append([img,choice])
# #        print('left appended')
        
#     if  f>0:
#         forwards.append([img,choice])
# #        print('forward appended')

#     if  r>0:
#         rights.append([img,choice])
# #       print('right appended')
    
#     if  b>0:
#         brakes.append([img,choice])
# #        print('brake appended')


# #actually balancing the data
# #forwards is forwards upto the length of lefts
# #or rights, whichever is longer
# #rights is rights upto the length of forwards
        
# forwards = forwards[:len(brakes)][:len(rights)]
# rights = rights[:len(forwards)]
# lefts = lefts[:len(rights)]
# #null = null[:len(lefts)]

# print(len(forwards))
# print(len(lefts))
# print(len(rights))
# print(len(brakes))
# #print(len(null))

# final_data = forwards + lefts + rights + brakes
# shuffle(final_data)
# final_data = np.array([final_data])
# print(final_data.shape)
# np.save('training_data_balanced_FORZA.npy',final_data)






















        
