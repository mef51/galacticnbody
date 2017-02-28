#!/usr/bin/python3

import os, shutil
import numpy as np
import plawt, imageio
from parsenbody import parseNBodyData

simulation = parseNBodyData('figure8.out')
numPlanets = simulation['n']
time = simulation['time']
planets = simulation['planets'] # first index is planet id,


# The indexing works like this: planets[planetid, posOrVel, time, component]

# plot an animation
with imageio.get_writer('figure8.mp4', mode='I', fps=20) as writer:
	for i, t in enumerate(time):
		currplot = {
			# 'filename': os.path.join(framesdir, 'frame' + str(i) + '.png'),
			'ylim': (-1, 1),
			'xlim': (-2,2),
			'keepOpen': True
		}

		for n, _ in enumerate(planets):
			currplot[n] = {'x': planets[n,0,i,0], 'y': planets[n,0,i,1], 'line': 'ko'}

		if i % 50 == 0:
			print('frame' + str(i) + '...')
		plt = plawt.plot(currplot)
		fig = plt.gcf()
		fig.canvas.draw()
		frame = fig.canvas.tostring_rgb()
		# print(type(frame))
		writer.append_data(imageio.imread(str(frame)))
		plt.close()

# with imageio.get_writer('figure8.mp4', mode='I', fps=20) as writer:
# 	for image in images:
#  		writer.append_data(image)
	# for filename in os.listdir(framesdir):
	#     image = imageio.imread(os.path.join(framesdir, filename))
	#     writer.append_data(image)
