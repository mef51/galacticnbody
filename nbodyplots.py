#!/usr/bin/python3

import os, shutil, glob
import numpy as np
import plawt, imageio
from parsenbody import parseNBodyData

# plot an animation
def saveanimation():
	framesdir = '__frames'
	if not os.path.exists(framesdir):
		os.mkdir(framesdir)

	for i, t in enumerate(time):
		filename = os.path.join(framesdir, 'frame' + str(i) + '.png')
		currplot = {
			'filename': filename,
			'ylim': (-1, 1),
			'xlim': (-2,2),
		}

		for n, _ in enumerate(planets):
			currplot[n] = {'x': planets[n,0,i,0], 'y': planets[n,0,i,1], 'line': 'ko'}

		if i % 50 == 0:
			print('frame' + str(i) + '...')
		plawt.plot(currplot)

	with imageio.get_writer('figure8.mp4', mode='I', fps=20) as writer:
		for filename in os.listdir(framesdir):
			image = imageio.imread(os.path.join(framesdir, filename))
			writer.append_data(image)

	shutil.rmtree(framesdir)

simdir = 'simulations'
figdir = 'figures'
for folder in [simdir, figdir]:
	if not os.path.exists(folder):
		os.mkdir(folder)

# simulation = parseNBodyData(os.path.join(simdir, 'figure8.out'))
# simulation = parseNBodyData(os.path.join(simdir, 'flingout.out'))
# simulation = parseNBodyData(os.path.join(simdir, 'flingout2.out'))
# simulation = parseNBodyData(os.path.join(simdir, 'chaos.out'))
# simulation = parseNBodyData(os.path.join(simdir, 'chaos2.out'))
# simulation = parseNBodyData(os.path.join(simdir, 'chaos3.out'))

for filename in glob.glob(os.path.join(simdir, '*.in')):
	title = os.path.splitext(os.path.basename(filename))[0]
	simulation = parseNBodyData(os.path.join(simdir, title + '.out'))
	numPlanets = simulation['n']
	time = simulation['time']
	planets = simulation['planets'] # # The indexing is: planets[planetid, posOrVel, time, component]

	tend = -1 # -1 takes the whole slice
	tstep = 20
	plawt.plot({
		'title': title,
		# Paths
		0: {'x': planets[0,0,:tend,0], 'y': planets[0,0,:tend,1], 'lw': 0.8, 'alpha': 0.5, 'line': 'k-'},
		1: {'x': planets[1,0,:tend,0], 'y': planets[1,0,:tend,1], 'lw': 0.8, 'alpha': 0.5, 'line': 'b-'},
		2: {'x': planets[2,0,:tend,0], 'y': planets[2,0,:tend,1], 'lw': 0.8, 'alpha': 0.5, 'line': 'r-'},
		# Starting Positions
		3: {'x': planets[0,0,0,0], 'y': planets[0,0,0,1], 'line': 'ko', 'ms': 10},
		4: {'x': planets[1,0,0,0], 'y': planets[1,0,0,1], 'line': 'bo', 'ms': 10},
		5: {'x': planets[2,0,0,0], 'y': planets[2,0,0,1], 'line': 'ro', 'ms': 10},
		# Final Positions
		6: {'x': planets[0,0,-1,0], 'y': planets[0,0,-1,1], 'line': 'k*', 'ms': 9, 'mfc': 'none'},
		7: {'x': planets[1,0,-1,0], 'y': planets[1,0,-1,1], 'line': 'b*', 'ms': 9, 'mfc': 'none'},
		8: {'x': planets[2,0,-1,0], 'y': planets[2,0,-1,1], 'line': 'r*', 'ms': 9, 'mfc': 'none'},
		# Time Sequence
		9:  {'x': planets[0,0,:tend,0][::tstep], 'y': planets[0,0,:tend,1][::tstep], 'lw': 0, 'line': 'ko', 'ms':2},
		10: {'x': planets[1,0,:tend,0][::tstep], 'y': planets[1,0,:tend,1][::tstep], 'lw': 0, 'line': 'bo', 'ms':2},
		11: {'x': planets[2,0,:tend,0][::tstep], 'y': planets[2,0,:tend,1][::tstep], 'lw': 0, 'line': 'ro', 'ms':2},
		'xlabel': 'x', 'ylabel': 'y',
		'filename': os.path.join(figdir, title + '.png'),
		'grid': True,
		'show': False
	})


exit()
numPlanets = simulation['n']
time = simulation['time']
planets = simulation['planets'] # first index is planet id,


# The indexing works like this: planets[planetid, posOrVel, time, component]

# plot the entire path
tend = -1 # -1 takes the whole slice
tstep = 20
plawt.plot({
	# Paths
	0: {'x': planets[0,0,:tend,0], 'y': planets[0,0,:tend,1], 'lw': 0.8, 'alpha': 1.0, 'line': 'k-'},
	1: {'x': planets[1,0,:tend,0], 'y': planets[1,0,:tend,1], 'lw': 0.8, 'alpha': 1.0, 'line': 'b-'},
	2: {'x': planets[2,0,:tend,0], 'y': planets[2,0,:tend,1], 'lw': 0.8, 'alpha': 1.0, 'line': 'r-'},
	# Starting Positions
	3: {'x': planets[0,0,0,0], 'y': planets[0,0,0,1], 'line': 'ko'},
	4: {'x': planets[1,0,0,0], 'y': planets[1,0,0,1], 'line': 'bo'},
	5: {'x': planets[2,0,0,0], 'y': planets[2,0,0,1], 'line': 'ro'},
	# Final Positions
	6: {'x': planets[0,0,-1,0], 'y': planets[0,0,-1,1], 'line': 'k*', 'ms': 9, 'mfc': 'none'},
	7: {'x': planets[1,0,-1,0], 'y': planets[1,0,-1,1], 'line': 'b*', 'ms': 9, 'mfc': 'none'},
	8: {'x': planets[2,0,-1,0], 'y': planets[2,0,-1,1], 'line': 'r*', 'ms': 9, 'mfc': 'none'},
	# Time Sequence
	9:  {'x': planets[0,0,:tend,0][::tstep], 'y': planets[0,0,:tend,1][::tstep], 'lw': 0, 'line': 'ko', 'ms':2},
	10: {'x': planets[1,0,:tend,0][::tstep], 'y': planets[1,0,:tend,1][::tstep], 'lw': 0, 'line': 'bo', 'ms':2},
	11: {'x': planets[2,0,:tend,0][::tstep], 'y': planets[2,0,:tend,1][::tstep], 'lw': 0, 'line': 'ro', 'ms':2},

	'filename': 'path.png',
	'grid': True,
	'show': False
})

# simulation = parseNBodyData(os.path.join(simdir, 'rings.out'))

# saveanimation()
