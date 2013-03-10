import unittest
import numpy as np
from getdata import getData
import anova
import compGroups
import distribution_normal
import gettingStarted
import multivariate
import pandas_intro
import univariate

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        t = np.arange(0,10,0.1)
        x = np.sin(t)
        self.data = x
        
    def test_dist_continuous(self):
        execfile('dist_continuous.py',{})
        
    def test_getdata(self):
        data = getData('altman_93.txt')
        self.assertEqual(data[0][0], 5260)
        
    def test_anova(self):
        anova.anova_oneway()
        anova.anova_interaction()
    
    def test_anovat(self):
        execfile('anovat.py')
        
    def test_compGroups(self):
        compGroups.oneProportion()
        compGroups.chiSquare()
        compGroups.fisherExact()
        
    def test_distribution_normal(self):
        distribution_normal.simple_normal()
        distribution_normal.shifted_normal()
        distribution_normal.many_normals()
        distribution_normal.check_normality()    
        distribution_normal.values_fromCDF()
        
    def test_dist_discrete(self):
        execfile('dist_discrete.py')
        
    def test_gettingStarted(self):
        gettingStarted.main()
        
    def test_modeling(self):
        execfile('modeling.py')
        
    def test_multivariate(self):
        multivariate.paired_data()    
        multivariate.unpaired_data()
        multivariate.regression_line()    
        multivariate.correlation()
        
    def test_pandas_intro(self):
        df = pandas_intro.simple_analysis()    
        pandas_intro.simple_plots(df)
        pandas_intro.example_altman()
        
    def test_residuals(self):
        execfile('residuals.py', {})
        
    def test_showStats(self):
        execfile('showStats.py', {})
        
    def test_ttest_1samp_notebook(self):
        execfile('ttest_1samp_notebook.py')
        
    def test_univariate(self):
        univariate.show_normal()    
        univariate.check_normality()
        univariate.check_mean()
    
        
if __name__ == '__main__':
    unittest.main()
    raw_input('Thanks for using programs from Thomas!')
    '''
    # should raise an exception 
    self.assertRaises(TypeError, savgol, np.arange(3), window_size=5)
    self.assertTrue(np.abs(1-smoothed[round(np.pi/2*10)]<0.001))
    self.assertEqual(firstDeriv[14], fD[14])
    '''
