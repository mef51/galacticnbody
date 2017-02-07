#!/usr/bin/python

from __future__ import division

datafile = "figure8.out"

numParticles = 0 # this shouldnt change but its printed out every time
time = [] # eg. [1, 2, 3, 4]
mass = [0] * numParticles
position = [[]] * numParticles
velocity = [[]] * numParticles

# this some fragile ass parsing
with open(datafile) as f:
	numParticles = int(f.readline())
	linenum = 2
	for lineTerminated in f:
		line = lineTerminated.rstrip()
		if line != "===":
			if linenum == 1:
				numParticles = int(line)
			elif linenum == 2:
				time.append(float(line))
			linenum += 1
		else:
			linenum = 1
