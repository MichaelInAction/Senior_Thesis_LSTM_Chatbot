
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

cbs = 0
bs = ''
X = []
cols = {'50':'r',
        '100': 'b',
        '300': 'g'}
plt.figure(figsize=(12,6))
legs = []
for filename in glob.iglob('modelsize*.txt'):
  bs = filename.split('-')[0][9:]
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

plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(legs, loc='upper right')
plt.show()
