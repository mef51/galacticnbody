#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

cdict = {}
cdict['red'] = ((0,0,0),(0,0,0))
cdict['blue'] = ((0,0,0),(0,0,0))
cdict['green'] = ((0,0,0),(0,0,0))
cdict['alpha'] = ((0,0,0), (1,1,1))
plt.scatter([0,1],[0,1], marker='*')

# segments =[[(0,0),(0.5,0.5)],[(0.5,0.5),(1,1)]]
segments = []
c = 0; N = 100
for i in range(0,N):
	inc = 1/N
	segments.append([(i*inc, i*inc), ((i+1)*inc,(i+1)*inc)])
segments = np.array(segments)

cmap = LinearSegmentedColormap('beep', cdict)
lc = LineCollection(segments, cmap=cmap, linewidth=1)
lc.set_array(np.linspace(-1, 1, 100))
ax = plt.gca()
ax.add_collection(lc)
plt.show()

