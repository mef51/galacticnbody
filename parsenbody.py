#!/usr/bin/python3

import numpy as np

datafile = "figure8.out"

def parseNBodyData(datafile):
	"""
	Returns a dictionary with the following fields:
	'n': number of particles
	'time': a 1d array of times
	'm': a 1d array of length 'n' with the masses of each planet
	'planets': a 2d array where the first index goes up to 'n' and
		and the second index is '0' for positions and '1' for 'velocities'.
		Both positions and velocities are arrays where each element is an
		array with 3 points representing the x, y and z components respectively.
	"""
	with open(datafile) as f:
		numPreLines = 2
		numParticles = int(f.readline())
		time = []
		masses = [0 for _ in range(numParticles)]
		positions = [[] for _ in range(numParticles)]
		velocities = [[] for _ in range(numParticles)]

		linenum = 2
		for lineTerminated in f:
			line = lineTerminated.rstrip()
			if line.count(',') == 0:
				if (linenum % numParticles) == 2:
					time.append(float(line))
				linenum += 1
			elif line.count(',') > 0:
				objectId = (linenum - (numPreLines + 1)) % numParticles
				for i, entry in enumerate(line.split(',')):
					if i == 0:
						masses[objectId] = float(entry.split(' ')[0])
					elif i == 1:
						pos = []
						for val in entry.split(' ')[:-1]:
							pos.append(float(val))
						positions[objectId].append(pos)

					elif i == 2:
						vel = []
						for val in entry.split(' '):
							vel.append(float(val))
						velocities[objectId].append(vel)
				linenum += 1
			if line == "===":
				linenum = 1

	data = np.array([time, positions, velocities])
	planets = [[] for _ in range(numParticles)]
	for i in range(0, numParticles):
		planets[i].append(positions[i])
		planets[i].append(velocities[i])

	return {
		'n': numParticles,
		'time': np.array(time),
		'm': np.array(masses),
		'planets': np.array(planets)
	}

