import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2


train_data = np.load('training_data_nissan_GTR_160X60_4.npy')

'''
#to verify 
for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test',img)
    print(choice)
    if cv2.waitKey(25) & 0xFF = ord('q'):
        cv2.destroyAllWindows()
        break
'''
df = pd.DataFrame(train_data)
#this counts the number of forward, left and right
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []
brakes = []
null =[]

#since we are not using LSTM cell
#so the order doesn't matter here
c =0
for data in train_data:
    img = data[0]
    choice = data[1]

    f = choice[0]
    b = choice[1]
    l = choice[2]
    r = choice[3]
    
    if  l>=0.05:
        lefts.append([img,choice])
#        print('left appended')
        
    if  f>0.05:
        forwards.append([img,choice])
#        print('forward appended')

    if  r>0.05:
        rights.append([img,choice])
#       print('right appended')
    
    if  b>0.05:
        brakes.append([img,choice])
#        print('brake appended')


#actually balancing the data
#forwards is forwards upto the length of lefts
#or rights, whichever is longer
#rights is rights upto the length of forwards
        
forwards = forwards[:len(brakes)][:len(rights)]
rights = rights[:len(forwards)]
lefts = lefts[:len(rights)]
#null = null[:len(lefts)]

print(len(forwards))
print(len(lefts))
print(len(rights))
print(len(brakes))
#print(len(null))

final_data = forwards + lefts + rights + brakes
shuffle(final_data)
np.save('training_data_balanced_nissan_GTR_4.npy',final_data)






















        
