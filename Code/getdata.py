'''Get data for the Python programs for statistics, FH OOe.
Most are from the tables in the Altman book "Practical Statistics for Medical Research.
I use these data quite often, so I have put those by default in a subdirectory
"data_altman". This function reads them from there.'''

'''
Author:  Thomas Haslwanter
Date:    March-2013
Version: 1.3
'''

from os.path import join
from numpy import genfromtxt
import os

def getData(inFile, subDir='data_altman'):
    '''Data are taken from examples in D. Altman, "Practical Statistics for Medical Research" '''
    dataDir = os.path.join('..','Data', subDir)
    inFile = join(dataDir, inFile)
    try:
        data = genfromtxt(inFile, delimiter=',')
    except IOError:
        print inFile + ' does not exist!'
        data = ()
    return data
    
if __name__ == '__main__':
    data = getData('altman_93.txt')
    print data
