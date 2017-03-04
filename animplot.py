#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import imageio
from numpy import sin, pi

print('Working...')
time = np.linspace(0, 10, 100)
with imageio.get_writer('test.mp4', mode='I', fps=24) as writer:
	for t in time:
		x = np.linspace(-2*pi,2*pi, 100)
		plt.plot(x, (x/(2*pi))*sin(t+x))
		plt.xlim(-2*pi, 2*pi), plt.ylim(-1.2, 1.2)
		fig = plt.gcf()
		fig.canvas.draw()
		data = fig.canvas.tostring_rgb()
		rows, cols = fig.canvas.get_width_height()

		imarray = np.fromstring(data, dtype=np.uint8).reshape(cols, rows, 3)
		writer.append_data(imarray)
		plt.close()
print('Done.')
