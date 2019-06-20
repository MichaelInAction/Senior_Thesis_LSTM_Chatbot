#Construct plot using output files

import os
import glob
import numpy as np
import matplotlib.pyplot as plt

testName = 'batchsize'
title = 'Batch Loss'
yLabel = 'Loss'
xLabel = 'Epoch'
saveLocation = '../Results/Batch-Loss-Graph.png'

cbs = 0
bs = ''
X = []
cols = {'1024':'r',
        '512': 'b',
        '128': 'g',
        '2': 'c'}
plt.figure(figsize=(12,6))
legs = []
for filename in glob.iglob(testName + '*.txt'):
  bs = filename.split('-')[0][len(testName):]
  print(bs)
  file = open(filename,'r')
  xl = file.read()[1:-3].split(',')
  x = np.array([float(i) for i in xl])
  #print(x)
  X.append(x)
  cbs += 1

  if cbs > 2:
    cbs = 0
    plt.plot(np.mean(X,axis=0),cols[bs])
    legs.append(bs+'-avg')
    for i in range(len(X)):
      plt.plot(X[i],cols[bs],alpha=0.1)
      legs.append(bs+'-'+str(i))
    X = []

plt.title(title)
plt.ylabel(yLabel)
plt.xlabel(xLabel)
plt.legend(legs, loc='upper right')
plt.show()
plt.savefig(saveLocation, bbox_inches='tight',dpi=350)
