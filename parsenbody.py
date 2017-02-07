#!/usr/bin/python

from __future__ import division

datafile = "figure8.out"

# this some fragile ass parsing
def parseNBodyData(datafile):
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
			elif line == "===":
				linenum = 1

	return {
		'n': numParticles,
		'time': time,
		'm': masses,
		'pos': positions,
		'vel': velocities
	}

print parseNBodyData('figure8.out')
