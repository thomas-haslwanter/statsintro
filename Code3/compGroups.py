''' Analysis of categorical data
- Analysis of one proportion
- Chi-square test
- Fisher exact test
- Cochran's Q test

'''

'''
Author:  Thomas Haslwanter
Date:    March-2014
Version: 1.3
'''

import numpy as np
import scipy.stats as stats
import pandas as pd
from statsmodels.sandbox.stats.runs import cochrans_q


def oneProportion():
    '''Calculate the confidence intervals of the population, based on a
    given data sample.
    The data are taken from Altman, chapter 10.2.1.
    Suppose a general practitioner chooses a random sample of 215 women from
    the patient register for her general practice, and fins that 39 of them
    have a history of suffering from asthma. '''

    # Get the data
    numTotal = 215
    numPositive = 39

    # --- >>> START stats <<< ---
    # Calculate the confidence intervals
    p = float(numPositive)/numTotal
    se = np.sqrt(p*(1-p)/numTotal)
    td = stats.t(numTotal-1)
    ci = p + np.array([-1,1])*td.isf(0.025)*se
    # --- >>> STOP stats <<< ---

    # Print them
    print('ONE PROPORTION ----------------------------------------')
    print(('The confidence interval for the given sample is {0:5.3f} to {1:5.3f}'.format(
        ci[0], ci[1])))
    
    return ci

def chiSquare():
    ''' Application of a chi square test to a 2x2 table.
    The calculations are done with and without Yate's continuity
    correction.
    Data are taken from Altman, Table 10.10:
    Comparison of number of hours' swimming by swimmers with or without erosion of dental enamel.
    >= 6h: 32 yes, 118 no
    <  6h: 17 yes, 127 no'''

    # Enter the data
    obs = np.array([[32, 118], [17, 127]])

    # --- >>> START stats <<< ---
    # Calculate the chi-square test
    chi2_corrected = stats.chi2_contingency(obs, correction=True)
    chi2_uncorrected = stats.chi2_contingency(obs, correction=False)
    # --- >>> STOP stats <<< ---

    # Print the result
    print('\nCHI SQUARE --------------------------------------------------')
    print(('The corrected chi2 value is {0:5.3f}, with p={1:5.3f}'.format(
        chi2_corrected[0], chi2_corrected[1])))
    print(('The uncorrected chi2 value is {0:5.3f}, with p={1:5.3f}'.format(
        chi2_uncorrected[0], chi2_uncorrected[1])))
    
    return chi2_corrected

def fisherExact():
    '''Fisher's Exact Test:
    Data are taken from Altman, Table 10.14
    Spectacle wearing among juvenile delinquensts and non-delinquents who failed a vision test
    Spectecle wearers: 1 delinquent, 5 non-delinquents
    non-spectacle wearers: 8 delinquents, 2 non-delinquents'''

    # Enter the data
    obs = np.array([[1,5], [8,2]])

    # --- >>> START stats <<< ---
    # Calculate the Fisher Exact Test
    # Note that by default, the option "alternative='two-sided'" is set;
    # other options are 'less' or 'greater'.
    fisher_result = stats.fisher_exact(obs)
    # --- >>> STOP stats <<< ---

    # Print the result
    print('\nFISHER --------------------------------------------------------')
    print(('The probability of obtaining a distribution at least as extreme '
    + 'as the one that was actually observed, assuming that the null ' +
    'hypothesis is true, is: {0:5.3f}.'.format(fisher_result[1])))
    
    return fisher_result

def cochranQ():
    '''Cochran's Q test: 12 subjects are asked to perform 3 tasks. The outcome of each task is "success" or 
    "failure". The results are coded 0 for failure and 1 for success. In the example, subject 1 was successful
    in task 2, but failed tasks 1 and 3.
    '''
    
    tasks = np.array([[0,1,1,0,1,0,0,1,0,0,0,0],
                      [1,1,1,0,0,1,0,1,1,1,1,1],
                      [0,0,1,0,0,1,0,0,0,0,0,0]])
    
    # I prefer a DataFrame here, as it indicates directly what the values mean
    df = pd.DataFrame(tasks.T, columns = ['Task1', 'Task2', 'Task3'])
    
    # --- >>> START stats <<< ---
    (Q, pVal) = cochrans_q(df)
    # --- >>> STOP stats <<< ---
    print('\nCOCHRAN\'S Q -----------------------------------------------------')
    print('Q = {0:5.3f}, p = {1:5.3f}'.format(Q, pVal))
    if pVal < 0.05:
        print("There is a significant difference between the three tasks.")
    
if __name__ == '__main__':
    oneProportion()
    chiSquare()
    fisherExact()
    cochranQ()

