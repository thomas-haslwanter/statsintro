''' Analysis of multivariate data
- Regression line
- Correlation

'''

'''
Author:  Thomas Haslwanter
Date:    March-2013
Version: 1.4
'''

import pandas as pd
from getdata import getData

def regression_line():
    '''Fit a line, using the powerful "ordinary least square" method of pandas'''
    
    # Get the data
    data = getData('altman_11_6.txt')
    
    df = pd.DataFrame(data, columns=['glucose', 'Vcf'])
    model = pd.ols(y=df['Vcf'], x=df['glucose'])
    print model.summary    
    
def correlation():
    '''Pearson correlation, and two types of rank correlation (Spearman, Kendall)
    Data from 24 type 1 diabetic patients, relating Fasting blood glucose (mmol/l) to
    mean circumferential shortening velocity (%/sec).'''
    
    # Get the data
    data = getData('altman_11_1.txt')
    
    # Bring them into the dataframe-format
    df = pd.DataFrame(data, columns=['age', 'fat'])
    
    # Calculate correlations
    corr = {}
    corr['pearson'] = df['age'].corr(df['fat'], method = 'pearson')
    corr['spearman'] = df['age'].corr(df['fat'], method = 'spearman')
    corr['kendall'] = df['age'].corr(df['fat'], method = 'kendall')
    
    print(corr)    
    
if __name__ == '__main__':
    regression_line()    
    correlation()
