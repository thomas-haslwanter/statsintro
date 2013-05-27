'''Introductions into using "Pandas": Simple work with two distributions
Pandas is a Python framework for statistical analysis. It allows you to label
and group data, etc.

'''

'''
Author : Thomas Haslwanter
Date : May 2013
Ver : 1.2
'''

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from os.path import join
from getdata import getData

def simple_analysis():
    '''Simple statistical analysis of dummy data'''
    
    # Generate dummy data
    # Since there are more rendeer than elephants, I cannot use a Python
    # dictionary. Instead I use "Series" from pandas. The other common pandas
    # datastructure is "DataFrame".
    data = {'rendeer' : pd.Series(stats.norm.rvs(size=70, loc=300, scale=50)),
        'elephants' : pd.Series(stats.norm.rvs(size=50, loc=500, scale=100))}
    df = pd.DataFrame(data)
    
    # Check some simple stats
    print 'Numbers'
    print df.count()
    
    print '\nMeans'
    print df.mean()
    
    print '\nMins'
    print df.min()
    
    print '\nMax'
    print df.max()
    
    # Confidence intervals for the mean elephant
    se =df['elephants'].std()/np.sqrt(df['elephants'].count())
    level = 0.975
    tval = stats.t.ppf(level, df['elephants'].count()-1)
    cis = df['elephants'].mean() + tval*se*np.array([-1., 1])
    print '95% CI for the weight of elephants: {0} - {1}'.format(cis[0], cis[1])
    
    # Is the weight of elephants different from 500 kg?
    testWeight = 500
    (tv, pv) = stats.ttest_1samp(df['elephants'].dropna(), testWeight)
    
    if pv < 0.05:
        print 'Elephants don''t weigh {0}kg'.format(testWeight)
    else:
        print 'Elephants weigh approximately {0}kg'.format(testWeight)
            
    # Are elephants heavier than rendeer?
    
    (tv, pv) = stats.ttest_ind(df['elephants'].dropna(), df['rendeer'])
    if pv < 0.05:
        if df['elephants'].mean() > df['rendeer'].mean():
            print 'Elephants are heavier than rendeer'
        else:
            print 'Rendeer are heavier than elephants'
    else:
        'Elephants and rendeer weigh the same'

    return df


def simple_plots(df):
    ''' Make some plots '''
    df.plot()
    plt.show()
    
    df.hist()
    plt.show()
    
    df.boxplot()
    plt.show()
    
    df.plot(style=['x','o'])
    plt.show()


def example_altman():
    '''Example from Altman "Practical statistics for medical research'''
    
    data = getData(r'data_altman\altman_94.txt')
    
    lean = pd.Series(data[data[:,1]==1,0])
    obese = pd.Series(data[data[:,1]==0,0])
    
    df = pd.DataFrame({'lean':lean, 'obese':obese})
    
    print(df.mean())
    plt.show()
    
    df.boxplot()
    plt.show()
    
    stats.ttest_ind(lean, obese)

if __name__ == '__main__':
    df = simple_analysis()    
    simple_plots(df)
    example_altman()
    
