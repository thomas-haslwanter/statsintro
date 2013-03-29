''' Analysis of Variance (ANOVA)
- Levene test
- ANOVA - oneway

'''

'''
Author:  Thomas Haslwanter
Date:    March-2013
Version: 1.2
'''

import scipy.stats as stats
import pandas as pd
from getdata import getData
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

def anova_oneway():
    ''' One-way ANOVA: test if results from 3 groups are equal. '''
    
    # Get the data
    data = getData('altman_910.txt')
    
    # Sort them into groups, according to column 1
    group1 = data[data[:,1]==1,0]
    group2 = data[data[:,1]==2,0]
    group3 = data[data[:,1]==3,0]
    
    # First, check if the variances are equal, with the "Levene"-test
    (W,p) = stats.levene(group1, group2, group3)
    if p<0.05:
        print('Warning: the p-value of the Levene test is <0.05: p={0}'.format(p))
    
    # Do the one-way ANOVA
    F_statistic, pVal = stats.f_oneway(group1, group2, group3)
    
    # Print the results
    print 'Altman 910:'
    print (F_statistic, pVal)
    if pVal < 0.05:
        print('One of the groups is significantly different.')
        
    # Elegant alternative implementation, with pandas & statsmodels
    df = pd.DataFrame(data, columns=['value', 'treatment'])    
    model = ols('value ~ C(treatment)', df).fit()
    print anova_lm(model)
    
if __name__ == '__main__':
    anova_oneway()
