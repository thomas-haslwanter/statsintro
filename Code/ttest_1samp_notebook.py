# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import scipy.stats as stats
import numpy as np

# generate the data
np.random.seed(12345)
normDist = stats.norm(loc=7, scale=3)
data = normDist.rvs(100)
checkVal = 6.5

# t-test
t, tProb = stats.ttest_1samp(data, checkVal)

# Comparison with corresponding normal distribution
mmean = np.mean(data)
mstd = np.std(data, ddof=1)
normProb = stats.norm.cdf(6.5, loc=mmean, scale=mstd/np.sqrt(len(data)))*2

# compare
print('The probability from the t-test is ' + \
'{0:4.3f}, and from the normal distribution {1:4.3f}'.format(tProb, normProb))

