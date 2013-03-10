''' Different discrete distribution functions.
- Binomial distribution
- Poisson distribution (PMF, CDF, and PPF)

'''

'''
Author:  Thomas Haslwanter
Date:    Jan-2013
Version: 1.1
'''

# Note: here I use the modular approach, which is more appropriate for scripts
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

bd1 = stats.binom(20, 0.5)
bd2 = stats.binom(20, 0.7)
bd3 = stats.binom(40, 0.5)
k = np.arange(40)
plt.plot(k, bd1.pmf(k), 'o-b')
plt.hold(True)
plt.plot(k, bd2.pmf(k), 'd-r')
plt.plot(k, bd3.pmf(k), 's-g')
plt.title('Binomial distribition')
plt.legend(['p=0.5 and n=20', 'p=0.7 and n=20', 'p=0.5 and n=40'])
plt.xlabel('X')
plt.ylabel('P(X)')
plt.show()

pd = stats.poisson(10)
plt.plot(k, pd.pmf(k),'x-')
plt.title('Poisson distribition - PMF')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.show()

k = np.arange(30)
plt.plot(k, pd.cdf(k))
plt.title('Poisson distribition - CDF')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.show()

y = np.linspace(0,1,100)
plt.plot(y, pd.ppf(y))
plt.title('Poisson distribition - PPF')
plt.xlabel('X')
plt.ylabel('P(X)')
plt.show()

