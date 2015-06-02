'''Plot a sine-wave

Author: Thomas Haslwanter
Date:   May-2015
Ver:    1.0

'''

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt

# Calculate the data
t = np.arange(0,10,0.1)
x = np.sin(t)

# Plot the data
plt.plot(t,x)
plt.show()
