'''Univariate data analysis

This script shows how to
- Use different methods of the normal distribution
- Generate random data and plot a histogram
- Check for normality (Kolmogorov-Smirnov)
- Use a t-test for a single mean
- Use a non-parametric test (Wilcoxon signed rank) to check a single mean 

'''

'''
Author: Thomas Haslwanter
Date:   Dec-2012
Version: 1.0
'''

from scipy.stats import norm
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from getdata import getData

def show_normal():
    '''Different aspects of the normal, Gaussian distribution.'''
    rv = norm()
    
    x = np.r_[-4:4:0.1]
    y = np.r_[0:1:0.001]
    
    ax = plt.subplot2grid((3,2),(0,0), colspan=2)
    #ax = plt.subplot(321)
    plt.plot(x,rv.pdf(x))
    plt.xlim([-4,4])
    plt.title('PDF')
    
    plt.subplot(323)
    plt.plot(x,rv.cdf(x))
    plt.xlim([-4,4])
    plt.title('CDF: cumulative distribution fct')
    
    plt.subplot(324)
    plt.plot(x,rv.sf(x))
    plt.xlim([-4,4])
    plt.title('SF: survival fct')
    
    plt.subplot(325)
    plt.plot(y,rv.ppf(y))
    plt.title('PPF')
    
    plt.subplot(326)
    plt.plot(y,rv.isf(y))
    plt.title('ISF')
    plt.tight_layout()
    plt.show()
    
def check_normality():
    '''Generate normally distributed data, and check normality them.'''
    
    # Generate and show a distribution
    plt.figure()
    myMean, mySD, numData = 50,10,500
    data = myMean + mySD*np.random.randn(numData)
    plt.hist(data)
    
    # Check for normality with Kolmogorov-Smirnov test
    _,pVal = stats.kstest((data-np.mean(data))/np.std(data,ddof=1), 'norm')
    if pVal > 0.05:
        print 'Data are probably normally distributed'
    
def check_mean():        
    '''Data from Altman, check for significance of mean value.
    Compare average daily energy intake (kJ) over 10 days of 11 healthy women, and
    compare it to the recommended level of 7725 kJ.'''
    
    # Get data from Altman
    data = getData('altman_91.txt')
    
    # Watch out: by default the SD is calculated with 1/N!
    myMean = np.mean(data)
    mySD = np.std(data, ddof=1)
    print 'Mean and SD: {0:4.2f} and {1:4.2f}'.format(myMean, mySD)
    
    # Confidence intervals
    tf = stats.t(len(data)-1)
    ci = np.mean(data) + stats.sem(data)*np.array([-1,1])*tf.isf(0.025)
    print 'The confidence intervals are {0:4.2f} to {1:4.2f}.'.format(ci[0], ci[1])
    
    # Check for significance
    checkValue = 7725
    t, prob = stats.ttest_1samp(data, checkValue)
    if prob < 0.05:
        print '{0:4.2f} is significantly different from the mean (p={1:5.3f}).'.format(checkValue, prob)
    
    # For not normally distributed data, use the Wilcoxon signed rank test
    (rank, pVal) = stats.wilcoxon(data-checkValue)
    if pVal < 0.05:
        issignificant = 'unlikely'
    else:
        issignificant = 'likely'
        
    print 'It is ' + issignificant + ' that the value is {0:d}'.format(checkValue)

if __name__ == '__main__':
    show_normal()    
    check_normality()
    check_mean()
