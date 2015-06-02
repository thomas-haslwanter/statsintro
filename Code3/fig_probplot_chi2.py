'''
Demonstration of the probplot of a non-normal distribution
'''

# author: Thomas Haslwanter, date: May-2015

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# additional packages
import mystyle

# Define the skewed distribution
chi2 = stats.chi2(3)

# Generate the data
x = np.linspace(0,10, 100)
y = chi2.pdf(x)
np.random.seed(12345)
numData = 100
data = chi2.rvs(numData)

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

'''
# To get an idea how probplot works, calculate the quantiles directly.
# in "probplot", Filliben's estimate is used, which changes the values slightly
data.sort()
mark_y = data[:-1]

nd = stats.norm()
mark_x = nd.ppf(np.arange(1,len(data))/numData)
axs[1].plot(mark_x, mark_y, 'rx-')
'''


mystyle.printout_plain('chi2pp.png')

plt.show()
