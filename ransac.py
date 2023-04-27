import numpy as np
import math

angle_min = -math.pi/2
angle_max = math.pi/2
laserdata = np.loadtxt("laserscan.dat")
num_data = len(laserdata)
theta = np.linspace(angle_min,angle_max,num_data)

