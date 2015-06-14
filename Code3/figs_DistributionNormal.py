''' Simple manipulations of normal distribution functions.
- Different displays of normally distributed data
- Compare different samples from a normal distribution
- Work with the cumulative distribution function (CDF)

'''

# Linked to text in: An Introduction to Statistics
# author: Thomas Haslwanter, date: July-2014

# Import standard packages
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.mlab import frange
import os
import seaborn as sns

myMean = 0
mySD = 3
x = np.arange(-5,15,0.1)
outDir = r'..\Images'

sns.set(context='poster', style='ticks', palette='deep')

def simple_normal():
    ''' Different aspects of a normal distribution'''
    # Generate the data
    x = np.arange(-4,4,0.1) # generate the desirded x-values
    x2 = np.arange(0,1,0.001)

    nd = stats.norm()   # First simply define the normal distribution;
                        # don't calculate any values yet

    
    # This is a more complex plot-layout: the first row
    # is taken up completely by the PDF
    ax = plt.subplot2grid((3,2),(0,0), colspan=2)

    plt.plot(x,nd.pdf(x))
    plt.xlim([-4,4])
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.yticks(np.linspace(0, 0.4, 5))
    plt.title('Normal Distribution - PDF')
    
    plt.subplot(323)
    plt.plot(x,nd.cdf(x))
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.xlim([-4,4])
    plt.ylim([0,1])
    plt.vlines(0, 0, 1, linestyles='--')
    plt.title('CDF: cumulative distribution fct')
    
    plt.subplot(324)
    plt.plot(x,nd.sf(x))
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.xlim([-4,4])
    plt.ylim([0,1])
    plt.vlines(0, 0, 1, linestyles='--')
    plt.title('SF: survival fct')
    
    plt.subplot(325)
    plt.plot(x2,nd.ppf(x2))
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.yticks(np.linspace(-4,4,5))
    plt.hlines(0, 0, 1, linestyles='--')
    plt.ylim([-4,4])
    plt.title('PPF')

    plt.subplot(326)
    plt.plot(x2,nd.isf(x2))
    plt.gca().xaxis.set_ticks_position('bottom')
    plt.gca().yaxis.set_ticks_position('left')
    plt.yticks(np.linspace(-4,4,5))
    plt.hlines(0, 0, 1, linestyles='--')
    plt.title('ISF')
    plt.ylim([-4,4])
    plt.tight_layout()
    
    outFile = 'DistributionFunctions.png'
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    
    plt.show()

def shifted_normal():
    '''PDF, scatter plot, and histogram.'''
    # Generate the data
    # Plot a normal distribution: "Probability density functions"
    myMean = [0,0,0,-2]
    mySD2 = [0.2,1,5,0.5]
    t = frange(-5,5,0.02)
    sns.set_palette('husl', 4)
    for mu,sigma in zip(myMean, np.sqrt(mySD2)):
        y = stats.norm.pdf(t, mu, sigma)
        plt.plot(t,y, label='$\mu={0}, \; \t\sigma={1:3.1f}$'.format(mu,sigma))
    plt.legend()
    plt.xlim([-5,5])
    plt.title('Normal Distributions')
    outFile = 'Normal_Distribution_PDF.png'
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    plt.show()
    
    # Generate random numbers with a normal distribution
    myMean = 0
    mySD = 3
    numData = 500
    data = stats.norm.rvs(myMean, mySD, size = numData)
    plt.scatter(np.arange(len(data)), data)
    plt.title('Normally distributed data')
    plt.xlim([0,500])
    plt.ylim([-10,10])
    plt.show()
    plt.close()
    
    #plt.hist(data)
    #plt.title('Histogram of normally distributed data')
    #plt.show()
    #plt.close()

def many_normals():
    '''Show multiple samples from the same distribution, and compare means.'''
    # Do this 25 times, and show the histograms
    numRows = 5
    numData = 50
    numData = 100
    myMean = 0
    mySD = 1
    plt.figure()
    for ii in range(numRows):
        for jj in range(numRows):
            data = stats.norm.rvs(myMean, mySD, size=numData)
            plt.subplot(numRows,numRows,numRows*ii+jj+1)
            plt.hist(data)
            plt.gca().set_xlim([-3, 3])
            plt.gca().set_xticks(())
            plt.gca().set_yticks(())
            plt.gca().set_xticklabels(())
            plt.gca().set_yticklabels(())
    
    plt.tight_layout()
    
    outFile = 'Normal_MultHist.png'
    
    saveTo = os.path.join(outDir, outFile)
    plt.savefig(saveTo, dpi=200)
    
    print('OutDir: {0}'.format(outDir))
    print('Figure saved to {0}'.format(outFile))
    plt.show()
    plt.close()
    
    # Check out the mean of 1000 normally distributded samples
    numTrials = 1000;
    numData = 100
    myMeans = np.ones(numTrials)*np.nan
    for ii in range(numTrials):
        data = stats.norm.rvs(myMean, mySD, size=numData)
        myMeans[ii] = np.mean(data)
    print(('The standard error of the mean, with {0} samples, is {1}'.format(numData, np.std(myMeans))))

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
    counts, bin_edges = np.histogram(data, bins=numbins, normed=True)
    cdf = np.cumsum(counts)
    cdf /= np.max(cdf)
    
    # compare with the exact CDF
    plt.step(bin_edges[1:],cdf)
    plt.hold(True)
    plt.plot(x, stats.norm.cdf(x, myMean, mySD),'r')
    
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
    print(('To get {0}% of the data, you need a threshold of {1:4.2f}.'.format((1-value)*100, icdf)))
    plt.show()

if __name__ == '__main__':
    many_normals()
    simple_normal()
    sns.set(font_scale=1.5, style='white')
    values_fromCDF()
    shifted_normal()

