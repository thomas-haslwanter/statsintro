# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# <nbformat>2</nbformat>
''' Different continuous distribution functions.
- Normal distribution
- Exponential distribution
- T-distribution
- Logistic distribution
- Lognormal distribution
[- Uniform distribution]

Author:  Thomas Haslwanter
Date:    Jan-2013
Version: 1.0

'''

from pylab import *
import scipy.stats as stats

# Normal distribution
x = linspace(-10,10,201)
plot(x, stats.norm.pdf(x))
hold(True)
plot(x, stats.norm.pdf(x, loc=2, scale=4), 'r')
title('Normal Distribution')
show()

# <codecell>

# Alternative coding style
#nd = stats.norm(loc=2, scale=2)
#plot(x, nd.pdf(x))
#show()

# Exponential distribution
plot(x, stats.expon.pdf(x))
hold(True)
plot(x, stats.expon.pdf(x, loc=-2, scale=4), 'r')
title('Exponential Distribution')
show()

# <codecell>

# Students' T-distribution
# ... with 4, and with 10 degrees of freedom (DOF)
td4 = stats.t(4)
td10 = stats.t(10)

plot(x, stats.norm.pdf(x))
hold(True)
plot(x, td4.pdf(x), 'r')
plot(x, td10.pdf(x), 'g')
legend(['normal', 't=4', 't=10'])
title('T-distributions')
show()

# Logistic distribution
plot(x, stats.norm.pdf(x))
hold(True)
plot(x, stats.logistic.pdf(x),'r')
legend(['Normal', 'Logistic'])
show()

# Lognormal distribution
plot(x, stats.lognorm.pdf(x,2))
title('Lognormal Distribution')
xlabel('x')
ylabel('lognorm(x)')
show()

xp = linspace(0,10,100001)
plot(log(xp), stats.lognorm.pdf(xp,2))
title('Lognormal Distribution')
xlabel('log(x)')
ylabel('lognorm(x)')
show()

# <codecell>

''' Simple manipulations of normal distribution functions.
- Different displays of normally distributed data
- Compare different samples from a normal distribution
- Check for normality
- Work with the cumulative distribution function (CDF)

Author:  Thomas Haslwanter
Date:    Jan-2013
Version: 1.1

'''

from pylab import *
import scipy.stats as stats

myMean = 0
mySD = 3
x = arange(-5,15,0.1)

def simple_normal():
    # Generate the data
    x = r_[-4:4:0.1]
    y = stats.norm.pdf(x)
    y_cdf = stats.norm.cdf(x)
    
    # Plot the distributions
    subplot(211)
    plot(x,y)
    title('Normal Distribution')
    ylabel('pdf(x)')
    
    subplot(212)
    plot(x,y_cdf)
    xlabel('x')
    ylabel('cdf(x)')    
    show()
    
def shifted_normal():
    '''PDF, scatter plot, and histogram.'''
    # Generate the data
    # Plot a normal distribution: "Probability density functions"
    myMean = 5
    mySD = 2
    y = normpdf(x, myMean, mySD)
    # or: y = stats.norm.pdf(x, myMean, mySD)
    plot(x,y)
    title('Shifted Normal Distribution')
    show()
    
    # Generate random numbers with a normal distribution
    numData = 500
    data = stats.norm.rvs(myMean, mySD, size = numData)
    plot(data, '.')
    title('Normally distributed data')
    show()
    
    hist(data)
    title('Histogram of normally distributed data')
    show()

def many_normals():
    '''Show multiple samples from the same distribution, and compare means.'''
    # Do this 25 times, and show the histograms
    numRows = 5
    numData = 50
    numData = 100
    for ii in range(numRows):
        for jj in range(numRows):
            data = stats.norm.rvs(myMean, mySD, size=numData)
            subplot(numRows,numRows,numRows*ii+jj+1)
            hist(data)
            gca().set_xticklabels(())
            gca().set_yticklabels(())
    
    tight_layout()
    show()
    
    # Check out the mean of 1000 normally distributded samples
    numTrials = 1000;
    numData = 100
    myMeans = ones(numTrials)*nan
    for ii in range(numTrials):
        data = stats.norm.rvs(myMean, mySD, size=numData)
        myMeans[ii] = mean(data)
    print('The standard error of the mean, with {0} samples, is {1}'.format(numData, std(myMeans)))

def check_normality():
    '''Check if the distribution is normal.'''
    # Are the data normally distributed?
    numData = 100
    data = stats.norm.rvs(myMean, mySD, size=numData)
    stats.normaltest(data)
    _ = stats.probplot(data, plot=plt)
    show()

def values_fromCDF():
    '''Calculate an empirical cumulative distribution function, compare it with the exact one, and
    find the exact point for a specific data value.'''
    
    # Generate normally distributed random data
    myMean = 5
    mySD = 2
    numData = 100
    data = stats.norm.rvs(myMean, mySD, size=numData)
    
    # Calculate the cumulative distribution function, CDF
    numbins = 20
    counts, bin_edges = histogram(data, bins=numbins, normed=True)
    cdf = cumsum(counts)
    cdf /= max(cdf)
    
    # compare with the exact CDF
    step(bin_edges[1:],cdf)
    hold(True)
    plot(x, stats.norm.cdf(x, myMean, mySD),'r')
    
    # Find out the value corresponding to the x-th percentile: the
    # "cumulative distribution function"
    value = 2
    myMean = 5
    mySD = 2
    cdf = stats.norm.cdf(value, myMean, mySD)
    print(('With a threshold of {0:4.2f}, you get {1}% of the data'.format(value, round(cdf*100))))
    
    # For the percentile corresponding to a certain value: 
    # the "inverse cumulative distribution function" 
    
    value = 0.025
    icdf = stats.norm.isf(value, myMean, mySD)
    print('To get {0}% of the data, you need a threshold of {1:4.2f}.'.format((1-value)*100, icdf))

if __name__ == '__main__':
    simple_normal()
    shifted_normal()
    many_normals()
    check_normality()    
    values_fromCDF()

# <codecell>


