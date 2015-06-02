''' Show different ways to present statistical data
This script is written in "MATLAB" or "ipython" style, to show how best to use Python interactively.
Note than in ipython, the "show()" commands are automatically generated.
The examples contain:
- scatter plots
- histograms
- errorbars
- boxplots
- violinplots
- cumulative density functions

'''

# Linked to text in: An Introduction to Statistics
# author: Thomas Haslwanter, date: Feb-2015

# First, import the libraries that you are going to need. You could also do
# that later, but it is better style to do that at the beginning.

# pylab imports the numpy, scipy, and matplotlib.pyplot libraries into the
# current environment

# Import standard packages
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import pandas as pd

# additional packages
import mystyle   # custom module to set fontsize, etc

def main():
    # Univariate data -------------------------
    # Generate data that are normally distributed
    x = np.random.randn(500)
    
    # Set the fonts the way I like them
    sns.set_context('poster')
    sns.set_style('ticks')
    #mystyle.set()
    
    # Scatter plot
    plt.scatter(np.arange(len(x)), x)
    plt.xlim([0, len(x)])
    mystyle.printout('scatterPlot.png', xlabel='x', ylabel='y', title='Scatter')
    
    # Histogram
    plt.hist(x)
    mystyle.printout('histogram_plain.png', xlabel='Data Values', ylabel='Frequency', title='Histogram, default settings')
    
    plt.hist(x,25)
    mystyle.printout('histogram.png', xlabel='Data Values', ylabel='Frequency', title='Histogram, 25 bins')
    
    # Cumulative probability density
    numbins = 20
    plt.plot(stats.cumfreq(x,numbins)[0])
    mystyle.printout('CumulativeFrequencyFunction.png', xlabel='Data Values', ylabel='Cumulative Frequency')
    
    # Boxplot
    # The ox consists of the first, second (middle) and third quartile
    plt.boxplot(x, sym='*')
    mystyle.printout('boxplot.png', xlabel='Values', title='Boxplot')
    
    plt.boxplot(x, sym='*', vert=False)
    plt.title('Boxplot, horizontal')
    plt.xlabel('Values')
    plt.show()
    
    # Errorbars
    x = np.arange(5)
    y = x**2
    errorBar = x/2
    plt.errorbar(x,y, yerr=errorBar, fmt='o', capsize=5, capthick=3)
    plt.xlim([-0.2, 4.2])
    plt.ylim([-0.2, 19])
    mystyle.printout('Errorbars.png', xlabel='Data Values', ylabel='Measurements', title='Errorbars')
    
    # Violinplot
    nd = stats.norm
    data = nd.rvs(size=(100))
    
    nd2 = stats.norm(loc = 3, scale = 1.5)
    data2 = nd2.rvs(size=(100))
    
    # Use pandas and the seaborn package for the violin plot
    df = pd.DataFrame({'Girls':data, 'Boys':data2})
    #sns.violinplot(df, color = ["#999999", "#DDDDDD"])
    sns.violinplot(df)
    
    mystyle.printout('violinplot.png')
    
if __name__ == '__main__':
    main()
