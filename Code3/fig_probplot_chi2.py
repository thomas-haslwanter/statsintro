'''
Demonstration of the probplot of a non-normal distribution
'''

# author: Thomas Haslwanter, date: July-2014

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import os.path
import mystyle

# Define the skewed distribution
chi2 = stats.chi2(3)

# Generate the data
x = np.linspace(0,10, 100)
y = chi2.pdf(x)
data = chi2.rvs(100)

# Arrange subplots
sns.set_context('paper')
sns.set_style('white')
mystyle.set(11)
fig, axs = plt.subplots(1,2)

# Plot distribution
axs[0].plot(x,y)
axs[0].set_xlabel('X')
axs[0].set_ylabel('PDF(X)')
axs[0].set_title('chi2(x), k=3')
sns.set_style('white')

x0, x1 = axs[0].get_xlim()
y0, y1 = axs[0].get_ylim()
axs[0].set_aspect((x1-x0)/(y1-y0))
#sns.despine()


# Plot probplot
plt.axes(axs[1])
stats.probplot(data, plot=plt)

x0, x1 = axs[1].get_xlim()
y0, y1 = axs[1].get_ylim()
axs[1].set_aspect((x1-x0)/(y1-y0))
#sns.despine()

mystyle.printout_plain('chi2pp.png')

plt.show()