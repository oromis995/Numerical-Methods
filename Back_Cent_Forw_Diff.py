import matplotlib.pyplot as plt 
import numpy as np

xyMatrix = [[805,0.710],[825,0.763],[845,0.907],
    [865,1.336],[885,2.169],[905,1.598],[925,0.916],
    [945,0.672],[965,0.615],[985,0.606]]
derivatives = []

for value in range(len(xyMatrix)):

	if value == 0:
		# First value used for forward difference
		derivatives.append((xyMatrix[value+1][1]-xyMatrix[value][1])/(xyMatrix[value+1][0]-xyMatrix[value][0]))
		print("first:",derivatives[value])
	elif value == len(xyMatrix)-1:
		# Last value for backward difference
		derivatives.append((xyMatrix[value][1]-xyMatrix[value-1][1])/(xyMatrix[value][0]-xyMatrix[value-1][0]))
		print("last",derivatives[value])
	else:
		# Central difference values
		derivatives.append((xyMatrix[value+1][1]-xyMatrix[value-1][1])/(xyMatrix[value+1][0]-xyMatrix[value-1][0]))
		print(value,":",derivatives[value])


plt.plot([x[0] for x in xyMatrix],derivatives,'-', color='black')

plt.xlabel("X")

plt.ylabel("F Prime")

plt.grid()
plt.show()